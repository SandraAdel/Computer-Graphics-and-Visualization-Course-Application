# Texture Mapping, Object Loading and Animation
**Texture Mapping**
- Draw a floor and put the full body on top of it and put a texture on the floor.
- Menu binned to the right mouse button to change the floor texture.
- We have 5 different floor texture options (Marble, Wood, Ice, Stones, Grass (Initial texture))

     ![ss4](https://user-images.githubusercontent.com/55870140/121246649-4082f900-c856-11eb-947c-d8be65f0f42a.png)  
     ![ss5](https://user-images.githubusercontent.com/55870140/121246930-82ac3a80-c856-11eb-8bf7-d24a44daa894.png)
     ![ss6](https://user-images.githubusercontent.com/55870140/121247283-eafb1c00-c856-11eb-8d97-8a8f8e92ab24.png)
     ![ss7](https://user-images.githubusercontent.com/55870140/121247598-46c5a500-c857-11eb-93bb-13d5ed715335.png)
     ![ss8](https://user-images.githubusercontent.com/55870140/121247881-9906c600-c857-11eb-80f7-04ea08332c2e.png)
     
**Object Loading and Animation**

3 Animations by sequence when running:
*1. Passing Football Animation:*
    *Object loaded: soccerball*
- The football is controlled by 2 parameters: ball_position_y and ball_position_z,
  where the uplifting of the ball is controlled by key 'u' and downlifting is controlled by key 'd'
  and their values are being printed along with robot angles by key 'p' in order to form correct positions
- Ball interaction is with robot is achieved by function playBall(ball_position_y, ball_position_z)

*2. Raising Cap Animation:*
