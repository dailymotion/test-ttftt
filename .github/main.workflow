workflow "Build and Release" {
  on = "push"
  resolves = ["Release"]
}

action "Release" {
  uses = "./action-release/"
  env = {
    VERSION = "100.0.0"
    USERNAME = "dailymotion"
    REPOSITORY = "tartiflette"
  }
}
