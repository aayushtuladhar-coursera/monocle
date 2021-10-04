-- | The monocle-api entrypoint
module Main (main) where

import Data.Text.IO (hPutStrLn)
import qualified Monocle.Api
import Relude

main :: IO ()
main = do
  args <- getArgs
  config <- fromMaybe "/etc/monocle/config.yaml" <$> lookupEnv "CONFIG"
  url <- fromMaybe "elastic:9200" <$> lookupEnv "ELASTIC_CONN"
  case args of
    ["--port", portStr] ->
      let port = fromMaybe (error $ "Could not read port: " <> toText portStr) $ readMaybe portStr
       in Monocle.Api.run port ("http://" <> toText url) config
    _ -> hPutStrLn stderr "usage: monocle-api --port PORT"
