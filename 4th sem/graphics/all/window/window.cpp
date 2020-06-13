#include<windows.h>
#include<GL/glut.h>
#include<stdio.h>
#include<stdlib.h>

void init(void){
    glClearColor(1.0,1.0,1.0,0.0);

}

void display(void ){
    glFlush();

}


int main(int argc,char** argv){
    glutInit(&argc,argv);
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB);
    glutInitWindowPosition(200,100);
    glutInitWindowSize(400,400);
    glutCreateWindow("Creating a Window");
    init();
    glutDisplayFunc(display);
    glutMainLoop();
}
