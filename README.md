# vortex2luau

vortex2luau is a little tool that takes map data from [Vortex](https://playvortex.io) and turns it into a Roblox Luau script, so you can bring Vortex maps into Roblox Studio.

Heads up: both Vortex and vortex2luau are still pretty early / rough around the edges. Once Vortex Studio actually comes out, this whole thing will probably need a full recode since I'm expecting their map system to be handled way better than it is now.

Also, vortex2luau is and always will be open-source, no plans to ever close it up. It's also getting renamed soon to **VorTools**, so don't be confused if you see that name floating around.

## What you'll need

- [Python](https://www.python.org/) installed
- Roblox Studio
- A Vortex map you actually want to convert

## How to use it

1. Grab some map data from `https://playvortex.io/api/maps` (official Vortex maps live here).
2. Copy that data and paste it into `model.json`. Just make sure the JSON isn't malformed, you can check it with a JSON validator.
3. Run `convert.py` easiest way is just double-clicking it. If it asks what app to open it with, pick the one called **exactly** "Python."
4. Open up `output.txt` and copy everything in it.
5. Pop open Roblox Studio, open the command bar, and paste it in there.
6. Hit enter and run it, your map should show up.

That's really it. Nothing too fancy, just a quick way to get maps from Vortex into Studio without doing it all by hand.

If something breaks, first thing to check is whether `model.json` is valid that's the most common thing that goes wrong. Otherwise feel free to poke around the code or open an issue.
