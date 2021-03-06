{
  "targets": [
    {
      "target_name": "wrapper",
      "sources": [
        "src/wrapper.cc",
        "src/game.cc",
        "src/game_eval.cc",
        "src/game_enum.cc",
        "src/hand_enum.cc",
        "src/enum.c"
      ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        "/usr/local/include",
        "/usr/local/include/poker-eval",
        "/usr/include/poker-eval"
      ],
      "libraries": [
        # "pkgconfig lib poker-eval",
        # "<!@(pkgconfig --libs poker-eval)",
      ]
    }
  ]
}