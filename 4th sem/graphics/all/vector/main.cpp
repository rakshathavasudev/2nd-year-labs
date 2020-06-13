#include<windows.h>
#include<GL/glut.h>
#include<stdio.h>
#include<GL/gl.h>
GLfloat vertices[]={200,10.0,
                   100.0,10.0,
                   100.0,50.0,
                   200.0,50.0 };
GLfloat color[]={1.0,0.0,0.0,
                0.0,1.0,0.0,
                0.0,0.0,1.0,
                1.0,0.0,1.0};
void display(){
    glClear(GL_COLOR_BUFFER_BIT);
    glEnableClientState(GL_VERTEX_ARRAY);
    glEnableClientState(GL_COLOR_ARRAY);
    glVertexPointer(2,GL_FLOAT,0,vertices);
    glColorPointer(3,GL_FLOAT,0,color);
    glDrawArrays(GL_POLYGON,0,10);
    glDisableClientState(GL_VERTEX_ARRAY);
    glDisableClientState(GL_COLOR_ARRAY);
    glFlush();
}
void init(){
    glClearColor(0.0,0.0,0.0,0.0);
    gluOrtho2D(0,200,0,200);
}
int main(int argc,char **argv){
    glutInit(&argc,argv);
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGBA|GLUT_DEPTH);
    glutInitWindowSize(500,500);
    glutInitWindowPosition(100,100);
    glutCreateWindow("Polygon_array");
    init();
    glutDisplayFunc(display);
    glutMainLoop();
    return 0;
}
