# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views


urlpatterns = [
    path('movies/', views.best_movie_list), # 총점 상위 10개
    path('movies/page=<int:page_id>/', views.movie_page), # 모든 영화 page로 20개씩
    path('movies/today/', views.today_movie_list), # 오늘 상영하는 영화
    path('movies/<int:movie_id>/', views.movie_detail), # movies/detail
    path('movies/today/<int:movie_id>/', views.today_movie_detail), # 오늘의 영화 detail
    path('movies/<int:movie_pk>/comments/', views.comment_create), # 영화에 댓글 추가
    path('comments/', views.comment_list), # 전체 댓글
    path('comments/<int:movie_pk>/', views.comment_detail), # 영화별 댓글 뭐 삭제 변경이런거
    path('movies/predicts/', views.predict_movie), #영화 예측
    # # 필수 작성
    # path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # # optional UI
    # path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]