from django.urls import path
from clone_pinterest import views

urlpatterns = [
    path('',views.home),
    path('about/',views.about ),
    path('business/',views.business ),
    path('press/',views.press ),
    path('login/',views.login ),
    path('signup/',views.signup ),
    
    path('dashboard/',views.dashboard ),
    path('explore/',views.explore),
    path('viewpin/<int:pin_id>',views.viewpin),
    path('board/<int:b_id>',views.board),
    path('search/',views.search),
    path('logout/',views.logout),
    path('addboard/',views.addboard),
    path('addpin/',views.addpin),
    path('choice/',views.choice),
    path('choice2/',views.choice2),
    path('editpin/<int:p_id>',views.editpin),
    path('deletepin/<int:p_id>',views.deletepin),
    path('addprofile/',views.addprofile),
    path('profile/',views.profile),
    path('editboard/<int:b_id>',views.editboard),
    path('deleteboard/<int:b_id>',views.deleteboard),
    path('addprofile/',views.addprofile),
    path('viewprofile/<int:p_id>',views.viewprofile),
    path('allpins/',views.allpins),
    path('savedpins/',views.savedpins),
    path('savepin/<int:p_id>',views.savepin),
    # path('updates/',views.updates),
    # path('message/',views.message),
    path('editprofile/<int:pro_id>',views.editprofile),
    path('deleteprofile/<int:pro_id>',views.deleteprofile),

]