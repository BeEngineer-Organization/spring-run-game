from direct.showbase.ShowBase import ShowBase
from direct.showbase.ShowBaseGlobal import globalClock
from panel_manager import GameStartScene, GameOverScene
from model_manager import Scene

MOVE_RIGHT = "move_right"
MOVE_LEFT = "move_left"
MOVE_UP = "move_up"


class Main(ShowBase):
    def __init__(self):
        super().__init__()
        # プレイヤーの変数

        # ゲームフラグ設定

        # キーボード入力設定

        # 車の設定

        # 車を発生させる時間

        # 当たり判定の設定

        # サウンドの設定

        # 毎フレーム読み込まれる処理を登録
        self.taskMgr.add(self.update, "update")

        # シーンの設定
        self.scene = Scene()

        # カメラの初期設定
        self.disableMouse()
        self.camera.setPos(0, -8, 3)
        self.camera.setHpr(0, -10, 0)

        # ゲームスタートシーンの読み込み
        self.game_start_scene = GameStartScene()
        self.game_start_scene.start_btn["command"] = self.start

        # ゲームオーバーシーンの読み込み
        self.game_over_scene = GameOverScene()
        self.game_over_scene.restart_btn["command"] = self.start
        self.game_over_scene.quit_btn["command"] = self.quit

        # 初期設定ではゲームオーバーシーンは非表示
        self.game_over_scene.game_over_screen.hide()

    # スタート画面でスタートが押された時にメインに移る関数
    def start(self):
        # ゲームスタート時には画面を非表示にする
        self.game_over_scene.game_over_screen.hide()
        self.game_start_scene.title_menu.hide()
        self.game_start_scene.title_menu_backdrop.hide()

        # プレイヤーの初期化処理
        if self.player != None:
            self.player.cleanup()

        # 効果音の切り替え

        # ゲームフラグをオンにする

        # プレイヤーのインスタンス化

        # カメラを追随する

        # プレイヤーが初期位置のときに車を発生させる処理

        # プレイヤーを物理ワールドにアタッチする

    # 初期化する関数
    def cleanup(self):
        self.is_contact = False
        self.is_game = False
        self.scene.physical_world.removeRigidBody(self.player.node())
        for car in self.cars:
            self.scene.physical_world.removeRigidBody(car.node())
            car.cleanup()
        self.cars = []

    # ゲームオーバー画面でやめるが押された時にメインにスタート画面に移る関数
    def quit(self):
        # ゲームオーバー画面を非表示にしてスタート画面を表示する
        self.game_start_scene.title_menu.show()
        self.game_start_scene.title_menu_backdrop.show()
        self.game_over_scene.game_over_screen.hide()

        # 効果音を切り替える

        # 初期化処理
        if self.player != None:
            self.player.cleanup()
            self.camera.reparentTo(base.render)

    # 車を出現させる関数
    def spawn_car(self, p_y):
        pass

    # 毎フレーム行う処理
    def update(self, task):
        return task.cont


app = Main()
app.run()
