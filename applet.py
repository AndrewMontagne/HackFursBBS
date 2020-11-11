from hackfursbbs.applets.splash import SplashScreen
from hackfursbbs.common.app_loop import AppLoop

boot_applet = SplashScreen()
loop = AppLoop(boot_applet, None)
loop.run()
