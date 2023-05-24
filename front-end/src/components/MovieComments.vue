<template>
  <div class="">
    <h3>Comments Create</h3>
      {{ user }}<br>
      {{ username }}<br>
      {{ email }}<br>
      <br><br><br><br>
      <label for="comment">댓글 : </label>
      <input @keyup.enter="commentCreate()" ref="cursor_comment" type="text" id="comment" v-model="comment_create">
      <input @click="commentCreate()" type="submit" value="확인">
      
    <div class="">
      <h3>Comments</h3>
        <div v-for="comment in comments"
        :key="comment.id" :comment="comment"
        >
        <p> user_id : {{ comment.user }} content : {{ comment.content }}<button @click="deleteComment(comment.comment_id)">X</button></p>
    </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieComments',
  components: {
  },

  data() {
    return {
      comments: null,
      comment: null,
      comment_create: null,
      user: this.$store.state.user,
      username: this.$store.state.username,
      email: this.$store.state.email,
      // nickname: this.$store.state.nickname
    }
  },
  created() {
    this.getUser()
    this.getComments()
  },
  methods: {
    getComments(){
        const id = this.$route.params.id
            // const movie_id = this.$route.params.id
        console.log()
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${ id }/allcomments/`,
      })
        .then((res) => {
            this.comments = res.data
            console.log('------------------------------')
            console.log(res.data)
            console.log(this.comments.comment_id)
        })
        .catch((err) => {
        console.log(err)
        })
    },
        deleteComment(id){
            const movie_id = this.$route.params.id
            console.log(id)
            console.log(movie_id)
// movies/<int:movie_id>/allcomments/<int:comments_pk>/
            axios({
                method: 'delete',
                url: `${API_URL}/api/v1/movies/${ movie_id }/allcomments/${id}/`,
                        data:{
                            movie_id, id
                        }
      })
        .then((res) => {
            this.comments = res.data
            console.log(res.data)
        })
        .catch((err) => {
        console.log(err)
        })
    },
    commentCreate(){
      const content = this.comment_create
      const id = this.$route.params.id
      const movie_id = id
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/${ id }/comments/`,
        data: {
          content, movie_id
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          
          console.log(res)
          // this.$router.push(`${API_URL}/api/v1/movies/${ id }/comments/`)
          // location.reload(true)
          this.getComments()
        })
        .catch((err) => {
        console.log(err)
        })
    },
    startCursor() {
      this.$refs.cursor_comment.focus()
    },
    getUser() {
      this.$store.dispatch('getUser')
    },
  }
}
</script>

<style>

</style>