<template>
  <div>
    <h1>Profile</h1>
    {{username}}
    <!-- <p>User Name : {{ user?.username }}</p>
    <p>User Email : {{ user?.email }}</p> -->
  </div>
</template>

<script>
// import axios from 'axios'
// const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  data() {
    return {
      username: this.username
    }
//   },
//   created() {
//     this.getUser()
//   },
//   methods: {
//     getUser() {
//       axios({
//         method: 'get',
//         url: `${API_URL}/api/v1/accounts/${ this.$route.params.id }/`,
//       })
//       .then((res) => {
//         console.log(res)
//         this.user = res.data
//       })
//       .catch((err) => {
//         console.log(err)
//       })
//     }
  }
}
</script>
