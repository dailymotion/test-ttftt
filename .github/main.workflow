workflow "Build and Release" {
  on = "push"
  resolves = ["Release"]
}

action "Release" {
  uses = "./action-release/"
  secrets = ["GITHUB_TOKEN"]
  env = {
    VERSION = "100.0.0"
    USERNAME = "dailymotion"
    REPOSITORY = "tartiflette"
  }
}
