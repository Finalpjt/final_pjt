<template>
  <div>
    {{ movie }}
    <h1>Detail</h1>
    <img style="height: 600px" :src="`https://image.tmdb.org/t/p/w220_and_h330_face/${ movie?.poster_path }`" alt="" srcset="">
    <p>글 번호 : {{ movie?.movie_id }}</p>
    <p>제목 : {{ movie?.eng_title }}</p>
    <p>한국어 제목 : {{ movie?.title }}</p>
    <p>장르 :
    <ul v-for="genre in movie?.genre" :key="genre">
        {{ genre.genre_ids }}
    </ul>
    </p>
    <p>청소년 관람 불가 : {{ movie?.adult }}</p>
    <p>영화 평점 : {{ movie?.vote_average }} </p>
    <p>영화 총점 : {{ movie?.popularity }} </p>
    <p>개봉일 : {{ movie?.release_date }} </p>
    <p>영화 줄거리 : {{ movie?.overview }}</p>
    <br><br>
    <p>관련 공식 영상</p>
    <ul v-for="(video, idx) in movie?.video" :key="video">
        <a :href="video.video">video {{ idx + 1 }}</a>
    </ul>
    <p>좋아요를 누른 사람 : {{ movie?.like_users }} </p>
    <button @click="getlikes()">ㅈㅇㅇ</button>
    <li v-if="movie?.like_users.indexOf(this.$store.state.pk) !== -1">
        <p>내가 좋아요를 누른 영화다 임마!</p>
    </li>
    <li v-else>
        <p>내가 좋아요를 누르지 않은 영화다 자시가!</p>
    </li>
    <!-- </button> -->
    <!-- <br><br> -->
    <br>
    <div>
    <h1>MovieRecommend</h1>
    <div class="row row-cols-1 row-cols-md-5 g-4">
    <div
    v-for="recommend_movie in recommend_movies" :key="recommend_movie.id" :movie="movie"
    >
    <div class="card" @click="reload()">
      
        <router-link :to="{
          name: 'DetailView',
          params: {id: recommend_movie.movie_id }}">
          <div class="card h-100">
          <img :src="`https://image.tmdb.org/t/p/w600_and_h900_bestv2/${recommend_movie.poster_path}`" alt="" srcset="">
          
          </div>
        </router-link>
      
    </div>
    </div>
    </div>
  </div>
    <br>
    <MovieComments/>
  </div>
</template>

<script>
import axios from 'axios'
// import MovieRecommend from '@/components/MovieRecommend.vue'
import MovieComments from '@/components/MovieComments.vue'
// import MovieCommentsList from '@/components/MovieCommentsList.vue'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  components: {
    // MovieRecommend, 
    MovieComments
  },

  data() {
    return {
      // allmovie: this.$store.state.movie,
      movie: null,
      poster_path: null,
      recommend_movies: null,
      user: this.$store.state.user,
      pk: this.$store.state.user.pk,
      username: this.$store.state.username,
      email: this.$store.state.email,
    }
  },
  created() {
    // console.log(this.user)
    // console.log('유저 네임 확인용')
    this.getUser(),
    this.getMovieDetail()
    // console.allmovie
  },
  methods: {
    getMovieDetail() {
      const movie_id = this.$route.params.id
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${ movie_id }`,
      })
      .then((res) => {
        // console.log(res.data)
        this.movie = res.data
        const movie_title = this.movie.title
        console.log(movie_title)

        axios({
          method: 'post',
          url: `${API_URL}/api/v1/movies/recommends/`,
          data: {
            movie: movie_title
          }
          })
          .then((res) => {
            // console.log(res)
            // console.log(res.data)
            this.recommend_movies = res.data
            // console.log(this.recommend_movies)

          })
          .catch((err) => {
            console.log(err)

          })
        })
      
      .catch((err) => {
        console.log(err)
      })
    },
    getUser() {
      this.$store.dispatch('getUser')
      
    },
    getlikes() {
      console.log(this.$route.params.id)
      const movie_id = this.$route.params.id
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/${ movie_id }/likes/`,
        data:{
          movie_id
        },
        headers:{
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        console.log(res)
        this.movie = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>
