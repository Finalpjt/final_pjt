<template>
  <div class="">
    <h3>Comments Create</h3>
      <label for="comment">댓글 : </label>
      <input @keyup.enter="commentCreate" ref="cursor_comment" type="text" id="comment" v-model="comment">
      <input @click="commentCreate" type="submit" value="확인">

    <!-- <p
    v-for="comment in comments" :key="comment.id" :comment="comment"
    ></p> -->
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
      comment: null,
    }
  },

  methods: {
    commentCreate(){
      const content = this.comment
      const id = this.$route.params.id
      const movie = id
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/${ id }/comments/`,
        data: {
          content, movie
        },
        // headers: {
        //   Authorization: `Token ${this.state.token}`
        // }
      })
        .then((res) => {
          
          console.log(res)
          // this.$router.push(`${API_URL}/api/v1/movies/${ id }/comments/`)
          // location.reload(true)
        })
        .catch((err) => {
        console.log(err)
        })
    },
    startCursor() {
      this.$refs.cursor_comment.focus()
    },
  }
}
</script>

<style>

</style>