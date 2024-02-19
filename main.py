import flet as ft
from flet import *
from sendMail import send_email

#-----edit & delete task class----------
class Modify(ft.UserControl):
    def __init__(self, task_val, delete_task):
        super().__init__()
        self.task_val = task_val
        self.delete_task = delete_task
    def build(self):
        self.display = ft.Checkbox(label=self.task_val)
        self.edit_val = ft.TextField(expand=True,max_length=35,max_lines=2)
        self.modify_view = ft.Row(
            controls=[
                self.display,
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip="Edit Task",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            icon=ft.icons.DELETE_OUTLINE,
                            tooltip="Delete Task",
                            on_click=self.delete,
                        ),

                    ],
                ),
            ],
        )
        self.edit = ft.Row(
            visible=False,
            controls=[
                self.edit_val,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip="Update Task",
                    on_click=self.save,
                ),
            ],
        )
        return ft.Column(controls=[self.modify_view, self.edit])

    def edit_clicked(self, e):
        self.edit_val.value = self.display.label
        self.modify_view.visible = False
        self.edit.visible = True
        self.update()

    def save(self, e):
        self.display.label = self.edit_val.value
        self.modify_view.visible = True
        self.edit.visible = False
        self.update()

    def delete(self, e):
        self.delete_task(self)

def main(page: ft.Page):
    #-----Display title on the top of the Window
    page.title= "PANDO" 
    #----Todo Function ---------
    def add_task(align: ft.MainAxisAlignment.SPACE_EVENLY ): 
        new_task = ft.TextField(hint_text="Add a task!",expand=True,max_length=35,max_lines=3)
        tasks_view= ft.Column()
        def add(e: ft.OnScrollEvent):
            task = Modify(new_task.value,delete_task)
            tasks_view.controls.append(task)
            new_task.value = ""
            page.update()
        def delete_task(task):
            tasks_view.controls.remove(task)
            page.update()
        return ft.Column(
            controls=
            [
            ft.Row(
                controls=[
                new_task,
                ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add,bgcolor=ft.colors.LIGHT_GREEN_400,),],),
            tasks_view,
                ],)
    page.update()
    #-----Homepage goals section routes to goals folders-------
    def goals_section(align: ft.MainAxisAlignment.SPACE_BETWEEN):
        return ft.Column([
            ft.Container(
                            ft.TextButton(text="Goals Folders",on_click=lambda _: page.go("/goals"),style=ft.ButtonStyle(
                                                  color={
                                                      ft.MaterialState.DEFAULT:ft.colors.BLACK
                                                  },
                                                  bgcolor=ft.colors.GREEN_50,
                                              )),
                            margin=5,
                            padding=5,
                            alignment=ft.alignment.center,
                            bgcolor="#8FB785",
                            border_radius=30,
                            ink=True,
                            ),
                        ft.Container(
            content=ft.Text("Click Goals Folders to head to your current goals"),
            margin=8,
            padding=20,
            border_radius=30,
            alignment=ft.alignment.top_left,
            ),
        ])
    
    #Creating a variable that holds the AppBar, our logo basically
    appName=ft.AppBar(title=ft.Text("PANDO"), center_title=True,bgcolor="#F9FFF9",toolbar_height=30)

    #-----Homepage high/low priority todo's, append the todo function to the page and enable scrolling
    today_todo_high_priority=ft.Column(
        spacing=10,
        height=200,
        scroll=ft.ScrollMode.ALWAYS,
        on_scroll_interval=0,
        on_scroll=add_task,
    )
    for i in range(1):
        today_todo_high_priority.controls.append(add_task(ft.OnScrollEvent))
    today_todo_low_priority=ft.Column(
        spacing=10,
        height=200,
        scroll=ft.ScrollMode.ALWAYS,
        on_scroll_interval=0,
        on_scroll=add_task,
    )
    for i in range(1):
        today_todo_low_priority.controls.append(add_task(ft.OnScrollEvent))
    
    #---------Homepage Content-------
    home_page= Container(
        content=ft.Column( 
            [
        #Creating settings button, and routing it to the correct page
            ft.IconButton(
                    icon=ft.icons.SETTINGS,
                    icon_color="green800", 
                    icon_size=40, 
                    tooltip="Settings",
                    on_click=lambda _: page.go("/settings")),

            ft.Container(
            content=ft.Text("today's to do"),
            margin=5,
            padding=20,
            border_radius=30,
            alignment=ft.alignment.top_left,
            bgcolor="#8FB785"),

        #Calling high and low priority columns
            ft.Text("High Priority"),
            ft.Container(today_todo_high_priority),
            ft.Text("Low Priority"),
            ft.Container(today_todo_low_priority),

        #Calling goals section routing function and passing the alignment through
        goals_section(ft.MainAxisAlignment.SPACE_BETWEEN),
            ]
        ))

  
    #-----Goal's folders page, contains 5 folders for user to add task------
    goals_folders_page= Container( 
        content=ft.Column(
            [
            ft.Container(
                content=ft.Text("Goals Folders"),
                margin=25,
                padding=20,
                border_radius=30,
                alignment=ft.alignment.top_left,
                bgcolor="#8FB785"),
                ft.Container(
                    alignment=ft.alignment.center,
                    height=500,
                    border_radius=30,
                    margin=5,
                    content=ft.Column(
                        [
                        ft.Container(
                            ft.TextButton("Goal 1",on_click=lambda _: page.go("/goal1"),
                                              style=ft.ButtonStyle(
                                                  color={
                                                      ft.MaterialState.DEFAULT:ft.colors.BLACK
                                                  },
                                                  bgcolor=ft.colors.GREEN_50,
                                              )),
                            margin=20,
                            padding=5,
                            alignment=ft.alignment.center,
                            bgcolor=ft.colors.ORANGE_100,
                            width=500,
                            height=50,
                            border_radius=10,
                            ink=True
                            ),
                          ft.Container(
                            ft.TextButton(text="Goal 2",on_click=lambda _: page.go("/goal2"),style=ft.ButtonStyle(
                                                  color={
                                                      ft.MaterialState.DEFAULT:ft.colors.BLACK
                                                  },
                                                  bgcolor=ft.colors.GREEN_50,
                                              )),
                            margin=20,
                            padding=5,
                            alignment=ft.alignment.center,
                            bgcolor="#CA7291",
                            width=500,
                            height=50,
                            border_radius=10,
                            ink=True,
                            ),

                          ft.Container(
                            ft.TextButton(text="Goal 3",on_click=lambda _: page.go("/goal3"),
                                          style=ft.ButtonStyle(
                                                  color={
                                                      ft.MaterialState.DEFAULT:ft.colors.BLACK
                                                  },
                                                  bgcolor=ft.colors.GREEN_50,
                                              )),
                            margin=20,
                            padding=5,
                            alignment=ft.alignment.center,
                            bgcolor="#6E9696",
                            width=500,
                            height=50,
                            border_radius=10,
                            ink=True,
                            ),

                          ft.Container(
                            ft.TextButton(text="Goal 4",on_click=lambda _: page.go("/goal4"),style=ft.ButtonStyle(
                                                  color={
                                                      ft.MaterialState.DEFAULT:ft.colors.BLACK
                                                  },
                                                  bgcolor=ft.colors.GREEN_50,
                                              )),
                            margin=20,
                            padding=5,
                            alignment=ft.alignment.center,
                            bgcolor=ft.colors.RED_200,
                            width=500,
                            height=50,
                            border_radius=10,
                            ink=True,
                            ),
                              ft.Container(
                            ft.TextButton(text="Goal 5",on_click=lambda _: page.go("/goal5"),style=ft.ButtonStyle(
                                                  color={
                                                      ft.MaterialState.DEFAULT:ft.colors.BLACK
                                                  },
                                                  bgcolor=ft.colors.GREEN_50,
                                              )),
                            margin=20,
                            padding=5,
                            alignment=ft.alignment.center,
                            bgcolor=ft.colors.PURPLE_100,
                            width=500,
                            height=50,
                            border_radius=10,
                            ink=True,
                            )
                        ]
                    )  
                ),
                ] 
            )
    )
    
    
    #----Goals description function 
    def goal_description(align: ft.MainAxisAlignment.SPACE_EVENLY):
        return ft.Column([
                        ft.TextField(label="Goals Description",
                         multiline=True,
                         min_lines=1,
                         max_lines=2,
                         max_length=100,
                         ),
        ])
    
    #----Routing function to goals folders page
    def goals_button(align: ft.MainAxisAlignment.SPACE_EVENLY):
        return ft.Container(
                padding=20,
                content=ft.Column([
            ft.ElevatedButton("Go back", on_click=lambda _: page.go("/goals"),style=ft.ButtonStyle(
                                                  color={
                                                      ft.MaterialState.DEFAULT:ft.colors.BLACK
                                                  },
                                                  bgcolor=ft.colors.GREEN_50,
                                              ),),]))
    
    #-----Goals 1 high/low priority todo's, append the todo function to the page and enable scrolling
    goal1_high_priority=ft.Column(
        spacing=10,
        height=300,
        scroll=ft.ScrollMode.ALWAYS,
        on_scroll_interval=0,
        on_scroll=add_task,
    )
    for i in range(1):
        goal1_high_priority.controls.append(add_task(ft.OnScrollEvent))
    goal1_low_priority=ft.Column(
        spacing=10,
        height=300,
        scroll=ft.ScrollMode.ALWAYS,
        on_scroll_interval=0,
        on_scroll=add_task,
    )
    for i in range(1):
        goal1_low_priority.controls.append(add_task(ft.OnScrollEvent))

    #--------Goal 1 folder page---------
    goal1_page=Container(
            content=ft.Column([
        ft.Container(
            content=ft.Text("Goal 1"),
            margin=8,
            padding=20,
            border_radius=30,
            alignment=ft.alignment.top_left,
            bgcolor="#8FB785"),
         ft.Container(goal_description(ft.MainAxisAlignment.SPACE_EVENLY)),
            ft.Text("High Priority"),
            ft.Container(goal1_high_priority),
            ft.Text("Low Priority"),
            ft.Container(goal1_low_priority),
            ft.Container(goals_button(ft.MainAxisAlignment.SPACE_EVENLY))
        ])
   
    )

    #-----Goals 2 high/low priority todo's, append the todo function to the page and enable scrolling
    goal2_high_priority=ft.Column(
        spacing=10,
        height=300,
        scroll=ft.ScrollMode.ALWAYS,
        on_scroll_interval=0,
        on_scroll=add_task,
    )
    for i in range(1):
        goal2_high_priority.controls.append(add_task(ft.OnScrollEvent))
    goal2_low_priority=ft.Column(
        spacing=10,
        height=300,
        scroll=ft.ScrollMode.ALWAYS,
        on_scroll_interval=0,
        on_scroll=add_task,
    )
    for i in range(1):
        goal2_low_priority.controls.append(add_task(ft.OnScrollEvent))
    
    #------Goals 2 folder page---------
    goal2_page=Container(
        content=ft.Column([
                ft.Container(
            content=ft.Text("Goal 2"),
            margin=8,
            padding=20,
            border_radius=30,
            alignment=ft.alignment.top_left,
            bgcolor="#8FB785"),
            ft.Container(goal_description(ft.MainAxisAlignment.SPACE_EVENLY)),
            ft.Text("High Priority"),
            ft.Container(goal2_high_priority),
            ft.Text("Low Priority"),
            ft.Container(goal2_low_priority),
            ft.Container(goals_button(ft.MainAxisAlignment.SPACE_EVENLY))

        ])
    )
    
    #-----Goals 3 high/low priority todo's, append the todo function to the page and enable scrolling
    goal3_high_priority=ft.Column(
        spacing=10,
        height=300,
        scroll=ft.ScrollMode.ALWAYS,
        on_scroll_interval=0,
        on_scroll=add_task,
    )
    for i in range(1):
        goal3_high_priority.controls.append(add_task(ft.OnScrollEvent))
    goal3_low_priority=ft.Column(
        spacing=10,
        height=300,
        scroll=ft.ScrollMode.ALWAYS,
        on_scroll_interval=0,
        on_scroll=add_task,
    )
    for i in range(1):
        goal3_low_priority.controls.append(add_task(ft.OnScrollEvent))

    #------Goals 3 folder page---------
    goal3_page=Container(
                content=ft.Column([
                ft.Container(
            content=ft.Text("Goal 3"),
            margin=8,
            padding=20,
            border_radius=30,
            alignment=ft.alignment.top_left,
            bgcolor="#8FB785"),
            ft.Container(goal_description(ft.MainAxisAlignment.SPACE_EVENLY)),
            ft.Text("High Priority"),
            Container(goal3_high_priority),
            ft.Text("Low Priority"),
            ft.Container(goal3_low_priority),
            ft.Container(goals_button(ft.MainAxisAlignment.SPACE_EVENLY))
        ])
    )

    #-----Goals 4 high/low priority todo's, append the todo function to the page and enable scrolling
    goal4_high_priority=ft.Column(
        spacing=10,
        height=300,
        scroll=ft.ScrollMode.ALWAYS,
        on_scroll_interval=0,
        on_scroll=add_task,
    )
    for i in range(1):
        goal4_high_priority.controls.append(add_task(ft.OnScrollEvent))
    goal4_low_priority=ft.Column(
        spacing=10,
        height=300,
        scroll=ft.ScrollMode.ALWAYS,
        on_scroll_interval=0,
        on_scroll=add_task,
    )
    for i in range(1):
        goal4_low_priority.controls.append(add_task(ft.OnScrollEvent))

    #------Goals 4 folder page--------
    goal4_page=Container(
                content=ft.Column([
                ft.Container(
            content=ft.Text("Goal 4"),
            margin=8,
            padding=20,
            border_radius=30,
            alignment=ft.alignment.top_left,
            bgcolor="#8FB785"),
            ft.Container(goal_description(ft.MainAxisAlignment.SPACE_EVENLY)),
            ft.Text("High Priority"),
            ft.Container(goal4_high_priority),
            ft.Text("Low Priority"),
            ft.Container(goal4_low_priority),
            ft.Container(goals_button(ft.MainAxisAlignment.SPACE_EVENLY))      
        ])
    )

    #-----Goals 5 high/low priority todo's, append the todo function to the page and enable scrolling
    goal5_high_priority=ft.Column(
        spacing=10,
        height=300,
        scroll=ft.ScrollMode.ALWAYS,
        on_scroll_interval=0,
        on_scroll=add_task,
    )
    for i in range(1):
        goal5_high_priority.controls.append(add_task(ft.OnScrollEvent))
    goal5_low_priority=ft.Column(
        spacing=10,
        height=300,
        scroll=ft.ScrollMode.ALWAYS,
        on_scroll_interval=0,
        on_scroll=add_task,
    )
    for i in range(1):
        goal5_low_priority.controls.append(add_task(ft.OnScrollEvent))

    #-----Goals 5 folder page--------
    goal5_page=Container(
                content=ft.Column([
                ft.Container(
            content=ft.Text("Goal 5"),
            margin=8,
            padding=20,
            border_radius=30,
            alignment=ft.alignment.top_left,
            bgcolor="#8FB785"),
            ft.Container(goal_description(ft.MainAxisAlignment.SPACE_EVENLY)),
            ft.Text("High Priority"),
            ft.Container(goal5_high_priority),
            ft.Text("Low Priority"),
            ft.Container(goal5_low_priority),
            ft.Container(goals_button(ft.MainAxisAlignment.SPACE_EVENLY))    
        ])
    )

    #----------Settings light/dark mode function-------------------
    def set(align: ft.MainAxisAlignment.SPACE_EVENLY):
        def theme_changed(e): #e 
            page.theme_mode = (
                ft.ThemeMode.DARK
                if page.theme_mode == ft.ThemeMode.LIGHT
                else ft.ThemeMode.LIGHT
            )
            c.label = (
            "Light theme" if page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
            )
        page.update()
        page.theme_mode = ft.ThemeMode.LIGHT
        c = ft.Switch(label="Light theme", on_change=theme_changed)
        return c
    
    #-------Send an email--------------------
    mail_status = ft.Text(text_align="center")
    page.snack_bar = ft.SnackBar(
        content=mail_status,
        bgcolor='#8FB785'
    )

    to = ft.Text("pando.reportproblem@gmail.com")
    subject = ft.TextField(label="Subject", border_radius=30, border="none",bgcolor=ft.colors.GREY)
    message = ft.TextField(label="Write your messsage", border_radius=20,max_lines=5,multiline=True, border="none",bgcolor="#8FB785")
    message_type = ft.Switch(label='HTML Mode', value=False, active_color='#8FB785')
   
    def send_mail(e):
        type_of_message = 'plain'
        if message_type.value == True:
            type_of_message = 'html'
        mail_status.value = send_email(to.value,subject.value,message.value,type_of_message)
        page.snack_bar.open = True
        page.update()

#--------Settings page=-----------------------
    settings_page=Container(
        content=ft.Column(
            controls=[
            ft.Container(
                content=ft.Text("Settings"),
                margin=8,
                padding=20,
                border_radius=30,
                alignment=ft.alignment.top_left,
                bgcolor="#8FB785"),

            ft.Container(
                alignment=ft.alignment.center,
                content=ft.Column(
                    [
                ft.Text("Instructions: Once changing the display toggle, go back to the home page to see the changes."),
                set(ft.MainAxisAlignment.SPACE_EVENLY),

            ])),
            
            to,
            subject,
            message,
            ft.Container(height=50),
            ft.IconButton(
                icon=ft.icons.SEND,
                icon_color=ft.colors.GREEN_400,
                icon_size=40,
                tooltip="Send Mail",
                on_click=send_mail
            ),
            ft.Container(height=10),

            ]
        )
    )

    page.update()

    #--------Change route function--------------
    def routing_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/", #home page
                [   
                    appName,
                    home_page,
                ],scroll='always'
            )
        )
        if page.route=="/settings":
            page.views.clear()
            page.views.append(
            ft.View(
                "/settings",
                [
                    ft.AppBar(title=ft.Text("PANDO"), center_title=True, bgcolor="#F9FFF9",toolbar_height=30),
                    settings_page,
                    ft.ElevatedButton("Exit", on_click=lambda _: page.go("/"),style=ft.ButtonStyle(
                                                  color={
                                                      ft.MaterialState.DEFAULT:ft.colors.BLACK
                                                  },
                                                  bgcolor=ft.colors.GREEN_50,
                                              )),

                ],
                scroll='always'
            )
        )
        if page.route== "/goals":
            page.views.clear()
            page.views.append(
                ft.View(
                    "/goals", #goals folders
                    [
                        ft.AppBar(title=ft.Text("PANDO"), center_title=True, bgcolor="#F9FFF9",toolbar_height=30),
                        goals_folders_page,
                        ft.ElevatedButton("Go home", on_click=lambda _: page.go("/"),style=ft.ButtonStyle(
                                                  color={
                                                      ft.MaterialState.DEFAULT:ft.colors.BLACK
                                                  },
                                                  bgcolor=ft.colors.GREEN_50,
                                              )),
                    ],scroll='always'
                )
            )
        if page.route== "/goal1" :
            page.views.clear()
            page.views.append(
                ft.View(
                    "/goals",
                    [
                        ft.AppBar(title=ft.Text("PANDO"), center_title=True, bgcolor="#F9FFF9",toolbar_height=30),
                        goal1_page,

                    ],scroll='always'
                )
            )
        if page.route== "/goal2" :
            page.views.clear()
            page.views.append(
                ft.View(
                    "/goals",
                    [
                        ft.AppBar(title=ft.Text("PANDO"), center_title=True, bgcolor="#F9FFF9",toolbar_height=30),
                        goal2_page,
                    ],scroll='always'
                )
            )
        if page.route== "/goal3" :
            page.views.clear()
            page.views.append(
                ft.View(
                    "/goals",
                    [
                        ft.AppBar(title=ft.Text("PANDO"), center_title=True, bgcolor="#F9FFF9",toolbar_height=30),
                        goal3_page,
                    ],scroll='always'
                )
            )

        if page.route== "/goal4" :
            page.views.clear()
            page.views.append(
                ft.View(
                    "/goals",
                    [
                        ft.AppBar(title=ft.Text("PANDO"), center_title=True, bgcolor="#F9FFF9",toolbar_height=30),
                        goal4_page,
                    ],scroll='always'
                )
            )
        if page.route== "/goal5" :
            page.views.clear()
            page.views.append(
                ft.View(
                    "/goals",
                    [
                        ft.AppBar(title=ft.Text("PANDO"), center_title=True, bgcolor="#F9FFF9",toolbar_height=30),
                        goal5_page,
                    ],scroll='always'
                )
            )


    #------event handler to update the views and calls for a page update
    page.on_route_change = routing_change
     #----Navigate through pages, helper method helps to update the page.route
    page.go(page.route) 
ft.app(target=main) #check desktop view

#ft.app(target=main, view=AppView.WEB_BROWSER) #check the web view