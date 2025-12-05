{
  description = "dev shell to run my advent of code solutions";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    utils.url = "github:numtide/flake-utils";
  };
  outputs = { self, nixpkgs, utils }: utils.lib.eachDefaultSystem (system:
    let
      pkgs = nixpkgs.legacyPackages.${system};
  in {

    devShells.default = pkgs.mkShell {
      packages = with pkgs; [
        aoc-cli
        python3
        uiua-unstable
        # (uiua-unstable.override {webcamSupport = true; windowSupport = true; })
      ] ++ lib.optionals (system == "x86_64-linux") [
        j
      ]
      ;
    };
  });
}
