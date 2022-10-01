<template>
  <form @submit.prevent modelAttribute="product" class="form loginwindow Login" action="/login" method="post" >
    <p>會員登入</p>
    <div class="mb-3 loginset">
      <label for="account" class="form-label ">帳號</label>
      <input v-model="account" type="text" class="form-control" id="account" name="account" />
    </div>
    <div class="mb-3 loginset">
      <label for="password" class="form-label ">密碼</label>
      <input v-model="password" type="password" class="form-control"/>
    </div>
    <button @click="submit()" class="btn btn-primary">登入</button>
  </form>
</template>

<script>

export default {
  name: "Account",
  data() {
    return {
      account: '',
      password: '',
    }
  },
  computed: {
  },
  components: {
  },
  methods: {
    submit(){
      if(this.account == ''){alert("請輸入帳號")}
      else if(this.password == '') {alert("請輸入密碼")}
      else{
        this.$http.get('http://localhost:8000/login/' + this.account + '/' + this.password)
        .then( r => {
        this.r = r.data
        if(r.data == "F") {
          console.log(r)
          alert("密碼錯誤")
        }
        else if(r.data == "U") {
          console.log(r)
          alert("帳號不存在")
        }
        else {
          console.log(r)
          alert("登入成功")
          localStorage.userid = r.data
          this.$router.push({name:'admin', params: { USER: localStorage.userid }})
        }
      })
        .catch( r => console.log(r))
      }
    },
  }
}
</script>


<style scoped>
.Login{
  background-color:aquamarine;
}
.loginwindow{
  font-size: 30px;
  text-align: center;
  width:40%;
  margin: auto;
  margin-top: 15px;
  padding: 30px;
  border: 1px solid #000000;
}
.loginset{
  font-size: 20px;
  width:60%;
  margin: auto;
}
.btn-primary{
  width:20%;
  margin: auto;
}
</style>