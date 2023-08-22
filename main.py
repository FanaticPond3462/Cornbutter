import sys
import argparse
import consolelog

#コマンドラインから実行された(モジュールとして呼び出されてない)ときに呼び出す
def main():
    #コマンドラインで指定された引数をパースする
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=str,help="Specify the path of the conversion source Java resource pack. The path of the source Java resource pack is the folder containing manifest.json")
    parser.add_argument("-o","--output", default="build",type=str,help="Please specify the destination folder.The standard is ./build/")
    parser.add_argument("-v", "--verbose", action="store_true",help="increase output verbosity")
    args = parser.parse_args()

    #verboseが呼ばれてるか判断した結果からロガー作成
    logger = consolelog.get_module_logger(__name__, args.verbose)
    if args.verbose:
        logger.debug("Verbose Flag is now enable!")#verbose通知
    
    #変換パイプライン構築
    pipeline = convert_pipeline(logger,args.verbose)
    #パイプラインで処理
    pipeline.process(args.source)
    #保存
    pipeline.write(args.output)
    #終了
    sys.exit(0)

#変換パイプライン
class convert_pipeline:
    #初期化
    def __init__(self,logger,verbose:bool = False) -> None:
        self.verbose = verbose
        self.logger = logger
    #処理
    def process(self,source) -> None:
        self.logger.info(source)
    #書き込み
    def write(self,output) -> None:
        self.logger.info(output)
        
#コマンドラインから実行された(モジュールとして呼び出されてない)ときに呼び出す
if __name__ == "__main__":main()