//*************************************************************************************************
//* (C) ColorfulSoft corp., 2021 - 2022. All Rights reserved.
//*************************************************************************************************

using System;
using System.Runtime.InteropServices;

namespace ColorfulSoft.DeOldify
{

    /// <summary>
    /// Multidimentional array of floating point data type.
    /// </summary>
    internal sealed unsafe class Tensor : IDisposable
    {

        /// <summary>
        /// Alignment boundary in bytes (16 for Vector4 SIMD compatibility).
        /// </summary>
        private const int Alignment = 16;

        /// <summary>
        /// Original unaligned pointer for freeing. Stored as long for x64 compatibility.
        /// </summary>
        private long _RawDataPtr;

        private long _RawShapePtr;

        /// <summary>
        /// Allocates aligned memory and stores the original pointer for freeing.
        /// </summary>
        private static float* AllocAlignedFloat(int count)
        {
            int size = count * sizeof(float);
            int total = size + Alignment + sizeof(long);
            IntPtr raw = Marshal.AllocHGlobal(total);
            long rawAddr = raw.ToInt64();
            // Reserve space before the aligned pointer to store the original pointer
            long alignedAddr = (rawAddr + sizeof(long) + Alignment - 1) & ~(long)(Alignment - 1);
            // Store original pointer just before the aligned block
            Marshal.WriteInt64(new IntPtr(alignedAddr - sizeof(long)), rawAddr);
            return (float*)alignedAddr;
        }

        private static int* AllocAlignedInt(int count)
        {
            int size = count * sizeof(int);
            int total = size + Alignment + sizeof(long);
            IntPtr raw = Marshal.AllocHGlobal(total);
            long rawAddr = raw.ToInt64();
            long alignedAddr = (rawAddr + sizeof(long) + Alignment - 1) & ~(long)(Alignment - 1);
            Marshal.WriteInt64(new IntPtr(alignedAddr - sizeof(long)), rawAddr);
            return (int*)alignedAddr;
        }

        private static void FreeAligned(long storedRawAddr)
        {
            if(storedRawAddr != 0)
            {
                Marshal.FreeHGlobal(new IntPtr(storedRawAddr));
            }
        }

        /// <summary>
        /// Data.
        /// </summary>
        public float* Data;

        /// <summary>
        /// Should destructor free Data?
        /// </summary>
        private bool __DisposeData = true;

        /// <summary>
        /// Shape.
        /// </summary>
        public int* Shape;

        /// <summary>
        /// Number of elements.
        /// </summary>
        public int Numel;

        /// <summary>
        /// Number of dimentions.
        /// </summary>
        public int Ndim;

        /// <summary>
        /// Default constructor.
        /// </summary>
        public Tensor()
        {
        }

        /// <summary>
        /// Initializes the tensor with specified shape.
        /// </summary>
        /// <param name="shape">Shape.</param>
        public Tensor(params int[] shape)
        {
            this.Ndim = shape.Length;
            this.Numel = 1;
            this.Shape = AllocAlignedInt(this.Ndim);
            this._RawShapePtr = Marshal.ReadInt64(new IntPtr((long)Shape - sizeof(long)));
            var Pshape = this.Shape;
            foreach(var Dim in shape)
            {
                this.Numel *= Dim;
                *Pshape++ = Dim;
            }
            this.Data = AllocAlignedFloat(this.Numel);
            this._RawDataPtr = Marshal.ReadInt64(new IntPtr((long)Data - sizeof(long)));
        }

        /// <summary>
        /// Disposes unmanaged resources of the tensor.
        /// </summary>
        void IDisposable.Dispose()
        {
            if((this.Data != null) && this.__DisposeData)
            {
                FreeAligned(this._RawDataPtr);
                this.Data = null;
            }
            if(this.Shape != null)
            {
                FreeAligned(this._RawShapePtr);
                this.Shape = null;
            }
        }

        /// <summary>
        /// Disposes unmanaged resources of the tensor.
        /// </summary>
        ~Tensor()
        {
            if((this.Data != null) && this.__DisposeData)
            {
                FreeAligned(this._RawDataPtr);
                this.Data = null;
            }
            if(this.Shape != null)
            {
                FreeAligned(this._RawShapePtr);
                this.Shape = null;
            }
        }

        /// <summary>
        /// Flattens 3d tensor to 2d.
        /// </summary>
        /// <returns>Tensor.</returns>
        public Tensor Flat3d()
        {
            var t = new Tensor();
            t.Data = this.Data;
            t._RawDataPtr = this._RawDataPtr;
            t.Ndim = 2;
            t.Numel = this.Numel;
            t.Shape = AllocAlignedInt(2);
            t._RawShapePtr = Marshal.ReadInt64(new IntPtr((long)t.Shape - sizeof(long)));
            t.Shape[0] = this.Shape[0];
            t.Shape[1] = this.Shape[1] * this.Shape[2];
            this.__DisposeData = false;
            return t;
        }

        /// <summary>
        /// Unflats the 2d tensor to 3d using specified size.
        /// </summary>
        /// <param name="h">Height.</param>
        /// <param name="w">Width.</param>
        /// <returns>Tensor.</returns>
        public Tensor Unflat3d(int h, int w)
        {
            var t = new Tensor();
            t.Data = this.Data;
            t._RawDataPtr = this._RawDataPtr;
            t.Ndim = 3;
            t.Numel = this.Numel;
            t.Shape = AllocAlignedInt(3);
            t._RawShapePtr = Marshal.ReadInt64(new IntPtr((long)t.Shape - sizeof(long)));
            t.Shape[0] = this.Shape[0];
            t.Shape[1] = h;
            t.Shape[2] = w;
            this.__DisposeData = false;
            return t;
        }

        /// <summary>
        /// Returns transposed version of this tensor.
        /// </summary>
        /// <returns>Tensor.</returns>
        public Tensor Transpose2d()
        {
            var t = new Tensor(this.Shape[1], this.Shape[0]);
            var px = this.Data;
            var py = t.Data;
            var width = this.Shape[1];
            var height = this.Shape[0];
            var n = 0;
            for(int i = 0; i < height; ++i)
            {
                for(int j = 0; j < width; ++j)
                {
                    py[j * height + i] = px[i * width + j];
                    ++n;
                }
            }
            return t;
        }

    }

}
