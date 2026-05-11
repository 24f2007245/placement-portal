<template>
    <nav>
      <span id="for_font" @click="indicate_index"><img src="../assets/logo.svg" ></span>

      <div id="nav_right">
        
        <span>role: {{ user_role }}</span>|
        <span id="u_eml">{{ user_email }}</span>
        <button @click="logout">Logout</button>
    </div>

    </nav>
</template>

<script setup>

const user_email=localStorage.getItem('email');
const user_role=localStorage.getItem('role');

function logout(){
  localStorage.clear();
  window.location.href="/login";
}

function indicate_index(){
  window.location.href='/';
}

</script>

<style scoped>
#for_font{
  margin-left: 20px;
}
nav{
  /* text-decoration:solid; */
  /* color: #2980B9; */
  position: sticky;
  top: 0;
  color: #f5f5f5;
  display: flex;
  justify-content:left;
  justify-content: space-between;
  /* justify-content: space-between; */
  background-color:#3b7ca6;
  padding: 10px;
  z-index: 1000;
  /* border: 1px solid gray; */
}
#nav_right{
  display: flex;
  gap: 10px;
  align-items: center;

}
img{
  width: 30px;
  transform: scale(1.6);
}
button{
  border: 1px solid #f5f5f5;
  background-color: #3b7ca6;
  color: #f5f5f5;
  padding: 5px;
}
button:hover{
  background-color: cadetblue;
  color: white;
  
}

@media(max-width:500px){
  #u_eml{
    display: none;
  }
}
</style>
    