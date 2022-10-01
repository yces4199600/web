<template>
  <form @submit.prevent modelAttribute="product" class="form loginwindow Signup" action="/signup" method="post" >
    <p>會員註冊</p>
    <div class="mb-3 loginset">
      <label for="account" class="form-label ">帳號</label>
      <input v-model="account" type="text" class="form-control " id="account" name="account" />
    </div>
    <div class="mb-3 loginset">
      <label for="password" class="form-label ">密碼</label>
      <input v-model="password" type="password" class="form-control "/>
    </div>
    <div class="mb-3 loginset">
      <label for="passwordcheck" class="form-label ">再次輸入密碼</label>
      <input v-model="passwordcheck" type="password" class="form-control "/>
    </div>
    <div class="mb-3 loginset">
      <label for="email" class="form-label ">電子信箱</label>
      <input v-model="email" type="text" class="form-control " id="email" name="email" />
    </div>
    <div class="mb-3 loginset">
      <label for="phone" class="form-label ">手機號碼</label>
      <input v-model="phone" type="text" class="form-control " id="phone" name="phone" />
    </div>
    <button @click="submit()" class="btn btn-primary">註冊</button>
  </form>
</template>

<script>
export default {
  name: "Signup",
  data() {
    return {
      account: '',
      password: '',
      passwordcheck:'',
      email: '',
      phone:''
    }
  },
  methods: {
    submit(){
      if(this.account == '' || this.password == '' || this.passwordcheck== '' || this.email == ''|| this.phone == '') alert("資料未齊全")
      else if(this.password != this.passwordcheck) alert("密碼驗證不符")
      else{
        this.$http.get('http://localhost:8000/signup/' + this.account + '/' + this.password + '/'+ this.email + '/' + this.phone)
      .then( r => {
        this.r = r.data
        if(r.data == "F") {
          console.log(r)
          alert("帳號已被註冊")
        }
        else {
          console.log(r)
          alert("註冊成功")
          this.$router.push({name:'login'})
        }
      })
      .catch( r => console.log(r))
      }
    },
  }
}
</script>


<style scoped>
.Signup{
  background-color:blanchedalmond;
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