#include<windows.h>
#include<GL/gl.h>
#include<GL/glut.h>
#include<GL/glu.h>
#include<stdio.h>
#include<stdlib.h>
float xc,yc,rx,ry;

inline int round(const float a){
    return int(a+0.5);
}

void display(void){
    int rx2=rx*rx;
    int ry2=ry*ry;
    int tworx2=2*rx2;
    int twory2=2*ry2;
    int p;
    int x=0;
    int y=ry;
    int px=0;
    int py=tworx2*y;
    void plotpoints(int,int,int,int);
    plotpoints(xc,yc,x,y);
    p=round(ry2-(rx2*ry)+(0.25*rx2));
    while(px<py){
        x++;
        px+=ry2+px;
        if(p<0)
            p+=ry2+px;
        else{
            y--;
            py-=tworx2;
            p+=ry2+px-py;

        }
        plotpoints(xc,yc,x,y);
    }

    p=round(ry2*(x+0.5)*(x+0.5)+rx2*(y-1)*(y-1)-rx2*ry2);
    while(y>0){
        y--;
        py-=tworx2;
        if(p>0)
            p+=rx2-py;
        else{
            x++;
            px+=twory2;
            p+=rx2-py+px;

        }
        plotpoints(xc,yc,x,y);

    }
    glFlush();
}
void plotpoints(int xc,int yc,int x,int y)
{
    glBegin(GL_POINTS);
    glVertex2i(xc+x,yc+y);
    glVertex2i(xc-x,yc+y);
    glVertex2i(xc+x,yc-y);
    glVertex2i(xc-x,yc-y);
    glEnd();
}

void init(void)
{
    glClearColor(1.0,0.0,0.0,0.0);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(-100,100,-100,100);
}

int main(int argc,char** argv ){
    printf("Enter the xcenter : ");
    scanf("%f",&xc);
    printf("Enter the ycenter : ");
    scanf("%f",&yc);
    printf("Enter x : ");
    scanf("%f",&rx);
    printf("Enter y : ");
    scanf("%f",&ry);
    glutInit(&argc, argv);
    glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize (500, 500);
    glutInitWindowPosition (100,100);
    glutCreateWindow ("Drawing Ellipse");
    init();
    glutDisplayFunc(display);
    glutMainLoop();

return 0;
}


