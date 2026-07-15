package top.jtmonster.jhentai

import android.os.Build
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.view.KeyEvent
import androidx.core.view.WindowCompat
import io.flutter.embedding.android.FlutterFragmentActivity
import io.flutter.embedding.engine.FlutterEngine
import io.flutter.plugin.common.EventChannel
import io.flutter.plugin.common.EventChannel.EventSink
import io.flutter.plugin.common.MethodChannel
import io.flutter.plugins.GeneratedPluginRegistrant
import org.opencv.android.OpenCVLoader

class MainActivity : FlutterFragmentActivity() {
    private var interceptVolumeEvent = false
    private lateinit var volumeMethodChannel: MethodChannel

    override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
        GeneratedPluginRegistrant.registerWith(flutterEngine)

        // 注册原生上色插件（MethodChannel）：安卓端上色引擎（OpenCV + ONNX Runtime + NNAPI）
        ColorizePlugin.registerWith(flutterEngine, applicationContext)

        volumeMethodChannel = MethodChannel(
            flutterEngine.dartExecutor.binaryMessenger,
            "top.jtmonster.jhentai.volume.event.intercept"
        )

        volumeMethodChannel.setMethodCallHandler { call, result ->
            if (call.method == "set") {
                val value = call.arguments<Boolean>()
                if (value != null) {
                    interceptVolumeEvent = value
                }
                result.success(null)
            } else {
                result.notImplemented()
            }
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        // 加载 OpenCV 原生库（org.opencv:opencv AAR 内置 .so），必须在任何 cv:: 调用前完成
        if (!OpenCVLoader.initDebug()) {
            android.util.Log.w("JHenTai", "OpenCV initDebug() 失败，上色相关功能将不可用")
        }

        WindowCompat.setDecorFitsSystemWindows(getWindow(), false)

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
            // Disable the Android splash screen fade out animation to avoid
            // a flicker before the similar frame is drawn in Flutter.
            splashScreen.setOnExitAnimationListener { splashScreenView -> splashScreenView.remove() }
        }

        super.onCreate(savedInstanceState)
    }

    override fun onKeyDown(keyCode: Int, event: KeyEvent?): Boolean {
        if (interceptVolumeEvent && (keyCode == KeyEvent.KEYCODE_VOLUME_UP || keyCode == KeyEvent.KEYCODE_VOLUME_DOWN)) {
            volumeMethodChannel.invokeMethod(
                "event",
                if (keyCode == KeyEvent.KEYCODE_VOLUME_UP) 1 else -1
            )
            return true
        }
        return super.onKeyDown(keyCode, event)
    }

    override fun onKeyUp(keyCode: Int, event: KeyEvent?): Boolean {
        if (interceptVolumeEvent && (keyCode == KeyEvent.KEYCODE_VOLUME_UP || keyCode == KeyEvent.KEYCODE_VOLUME_DOWN)) {
            return true
        }
        return super.onKeyUp(keyCode, event)
    }

    override fun onDestroy() {
        volumeMethodChannel.setMethodCallHandler(null)
        super.onDestroy()
    }
}
