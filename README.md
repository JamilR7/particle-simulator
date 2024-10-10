# Simple Gravity Simulator
--------------------------

There are different modes that determine how the particles move which can be activated via keystrokes. Currently, there are two modes that can be combined, a mode for particles to fall to the ground and a mode for particles to be attracted towards each other to form cell-like structures.

F to make the particles fall to the floor<br/>T to make the particles gravitate towards each other

There is also 2D collision dynamics incorporated, particles will glow when a collision check is being computed.

I plan to add options to adjust particle properties and toggle more types of particle behaviour once I have optimised the algorithms.

![Animation-new](https://github.com/user-attachments/assets/43526c54-5261-409c-82ad-e070b0ab4643)

Here we can see the 2D collisions taking place, particles will move in random directions and will glow yellow when a collision check is being processed. To optimise performance, we using sorting algorithms and the transitive property of inequality to avoid collision detection with unnecessary particles.

![Animation-new2](https://github.com/user-attachments/assets/4ea72d58-c9d7-40cd-9a82-5f5b566c0c32)

Gravity applied with a coefficient of restitution.

![Animation-new3](https://github.com/user-attachments/assets/bdf67d66-d9af-4eff-b073-5d41077fddee)

Formation of cell-like structures with repulsion to avoid particles collapsing. 

![Animation-1](https://github.com/user-attachments/assets/90c65ac3-8b85-487d-86b4-3a6402ec51b7)

Particles show chaotic behavior, continuously revolving around each other and forming boomerang-like motions as they are drawn toward the center of mass.
