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

A) 3 Animations by sequence when running:

*1. Passing Football Animation:*
    *Object loaded: soccerball (Animation Interaction with Object)*
- The football is controlled by 2 parameters: ball_position_y and ball_position_z,
  where the uplifting of the ball is controlled by key 'u' and downlifting is controlled by key 'd'
  and their values are being printed along with robot angles by key 'p' in order to form correct positions
- Ball interaction with robot is achieved by function playBall(ball_position_y, ball_position_z)

![2021-06-09 (19)](https://user-images.githubusercontent.com/81769303/121265751-96d55380-c8b9-11eb-9777-f893d670abca.png)

*2. Raising Cap Animation:*
    *Object loaded: casquette (Animation Interaction with Object)*
- The cap is controlled by 1 parameter: casquette_position_y,
  where the uplifting of the cap in the y direction is controlled by key 'c' and downlifting by key 'C'
  and its value is being printed along with other values as stated before to form correct positions
- Cap interaction with robot is achieved by function raiseCasquette(casquette_position_y)

![2021-06-09 (20)](https://user-images.githubusercontent.com/81769303/121265768-9f2d8e80-c8b9-11eb-993a-1d728d26ec87.png)

*3. Walking Animation:*
    *Object loaded: None (Animation Interaction without Object)*
- This action is controlled by 1 parameter: step_forward,
  where the stepping forward process is controlled by key 'o'
  and its value is being printed along with other values as stated before to form correct positions
- The walking process is achieved by function walk(step_forward)

![2021-06-09 (21)](https://user-images.githubusercontent.com/81769303/121265788-a6ed3300-c8b9-11eb-88b0-fd9aaa905f42.png)

B) To make sense of the environment:
- The casquette object is chosen to be a sports one not a formal one
- Another object is loaded: football_goal to make sense of a football field
  and is positioned using function drawFootBallGoal()

