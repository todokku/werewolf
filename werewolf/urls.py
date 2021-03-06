from django.urls import path
from werewolf import views

urlpatterns = [
    path('login', views.login_action, name="login"),
    path('register', views.register_action, name="register"),
    path('logout', views.logout_action, name='logout'),
    path('profile', views.getProfile, name='profile'),
    path('image/<int:id>', views.get_image, name="image"),
    path('rule', views.rule, name='rule'),
    path("character", views.character, name="character"),
    path('', views.getGameLobby, name="lobby"),
    path('create-room', views.createRoom, name="createRoom"),
    path('get-players/<int:roomID>', views.getPlayers, name="getPlayers"),
    path('ready/<int:roomID>', views.ready, name="ready"),
    path('get-username/<int:userID>', views.getUsername, name="getUsername"),
    path('wolf_kill_1/<int:roomID>/<userID>/<int:killedID>', views.wolf_kill_1, name="wolf_kill_1"),
    path('get-Usernumber/<int:roomID>', views.getUsernumber, name="getUsernumber"),
    path('get-role/<int:userID>', views.getRole, name="getRole"),
    path('search-by-id/<int:id>/<str:pw>', views.searchByRoomID, name="searchByRoomID"),
    path('search-by-mode/<str:diff>/<str:num>', views.searchByMode, name="searchByMode"),
    path('join-room/<int:roomID>', views.joinRoom, name="joinRoom"),
    path('exit-room/<int:roomID>', views.exitRoom, name="exitRoom"),
    path('start/<int:roomID>', views.start_game, name="start"),
    path('start_game_again/<int:roomID>', views.start_game_again, name="start_game_again"),
    path('vote/<int:roomID>/<userID>/<int:voteID>', views.vote, name="vote"),
    path('select_card', views.select_card, name="select_card"),
    path('check_card/<int:roomID>', views.check_card, name='check_card'),
    path('start_game', views.start_game, name='start_game'),
    path('refresh-page', views.refresh_page),
    path('seer_select/<int:roomID>/<userID>/<int:selectedID>', views.seer_select, name="seer_select"),
    path('day_conclude_wolf/<int:roomID>', views.day_conclude_wolf, name="day_conclude_wolf"),
    path('doctor_heal/<int:roomID>/<userID>/<int:healedID>', views.doctor_heal, name="doctor_heal"),
    path('doctor_not_heal/<int:roomID>/<userID>/<int:healedID>', views.doctor_not_heal, name="doctor_not_heal"),
    # path('day_conclude_doctor/<int:roomID>', views.day_conclude_doctor, name="day_conclude_doctor")
    path('day_speak/<int:roomID>/<userID>', views.day_speak, name="day_speak"),
    path('seer_select2/<int:roomID>/<userID>/', views.seer_select2, name='seer_select2'),
    path('doctor_heal2/<int:roomID>/<userID>/', views.doctor_heal2, name='doctor_heal2'),
    path('end_game/<int:roomID>', views.end_game, name="end_game"),
    path('voice_chat', views.voiceChat, name="voice_chat"),
    path('kill_again/<int:roomID>', views.kill_again, name='kill_again'),
    path('refresh-lobby', views.refreshLobby, name="refresh-lobby"),
    path('remove_empty_room', views.removeEmptyRoom, name='remove_empty_room'),

]
