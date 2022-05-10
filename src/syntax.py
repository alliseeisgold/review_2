syntax = "syntax"
example = "for example"
description = "description"
helper = {
    "/start or /restart": {
        syntax: " ",
        example: "/start",
        description: "Bot welcomes you and introduces itself."
    },
    "/tracks": {
        syntax: "/tracks singer_name",
        example: "/tracks justin bieber",
        description: "Shows you top tracks of a given artist."
    },
    "/charts": {
        syntax: "/charts country_code",
        example: "/charts ru",
        description: """Shows you top tracks of a given country.\
    Statics of some countries are not displayed in it, so by default\
    it shows the top tracks of the USA."""
    },
    "/chart_artists": {
        syntax: "/char_artists country_code",
        example: "/char_artists ru",
        description: """The same as the description of /charts command.\
        But instead of top tracks it shows most famous singers in the region.
        """
    },
    "/lyrics": {
        syntax: "/lyrics music_name",
        example: "/lyrics genesis",
        description: "Shows the music lyrics."
    }
}
