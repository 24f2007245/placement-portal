<template>
    <nav>
      <span><strong>Placements Cell&nbsp;</strong></span>

      <div id="nav_right">
        
        <span>role: {{ user_role }}</span>|
        <span>{{ user_email }}</span>
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

</script>

<style scoped>
nav{
  /* text-decoration:solid; */
  color: #2980B9;
  display: flex;
  justify-content:left;
  justify-content: space-between;
  /* justify-content: space-between; */
  background-color:#f5f5f5;
  padding: 10px;
}
#nav_right{
  display: flex;
  gap: 10px;
  align-items: center;

}
</style>
    