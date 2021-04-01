#include <stdio.h>
 
#include <math.h>
 
int main()
 
{
       float i = 0.314;
       float j = 0.25;
       float k = 6.25;
       float l=27;
       float sin_value = sin(i);
       float cos_value = cos(i);
       float tan_value = tan(i);
       float sec_value = sec(j);
       float cosec_value = cosec(j);
       float cot_value = cot(j);
       float log_value = log(k);
       float cube_value = cbrt(l);
       printf("The value of sin(%f) : %f \n", i, sin_value);
       printf("The value of cos(%f) : %f \n", i, cos_value);
       printf("The value of tan(%f) : %f \n", i, tan_value);
       printf("The value of sec(%f) : %f \n", j, sec_value);
       printf("The value of cosec(%f) : %f \n", j, cosec_value);
       printf("The value of cot(%f) : %f \n", j, cot_value);
       printf("The value of log(%f) : %f \n", k, log_value);
       printf("The value of cube(%f) : %f \n",l, cube_value);
       return 0;
}