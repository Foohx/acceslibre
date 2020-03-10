module Data.Activite exposing
    ( Activite
    , Slug
    , decode
    , findBySlug
    , slugFromString
    , slugParser
    , slugToString
    )

import Json.Decode as Decode exposing (Decoder)
import Json.Decode.Pipeline as Pipe
import Url.Parser as Parser exposing (Parser)


type Slug
    = Slug String


type alias Activite =
    { nom : String
    , slug : Slug
    , count : Maybe Int
    }


decode : Decoder Activite
decode =
    Decode.succeed Activite
        |> Pipe.required "nom" Decode.string
        |> Pipe.required "slug" (Decode.map Slug Decode.string)
        |> Pipe.optional "count" (Decode.maybe Decode.int) Nothing


findBySlug : Slug -> List Activite -> Maybe Activite
findBySlug slug =
    List.filter (.slug >> (==) slug) >> List.head


slugToString : Slug -> String
slugToString (Slug slug) =
    slug


slugFromString : String -> Slug
slugFromString string =
    Slug string


slugParser : Parser (Slug -> a) a
slugParser =
    Parser.custom "ActiviteFromSlug" (Just << Slug)
