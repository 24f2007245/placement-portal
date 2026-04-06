<script setup>
const user_email=localStorage.getItem('email').toUpperCase()
// const user_role= localStorage.getItem('role').toUpperCase()
const user_name=localStorage.getItem('user_name').toUpperCase()
</script>
<template>
    <div id="main">
        <h1>Welcome {{ user_name }}</h1><h3>{{ user_email }}</h3>
        <!-- <label for="search"><h3>Search</h3></label> -->
        <span><input type="search" id="search" placeholder="search"></span>
        <span><button type="submit">find</button></span>
        

    </div>

</template>

<style scoped>
#main{
    /* background-color: #f5f5f5; */
    width: 280px;
    max-width: 100%;
    flex-shrink: 0;
    /* height: 100%; */
    color: #2980B9;
    margin: 30px;
    display: flex;
    flex-direction: column;
    /* position:static; */
}

h1, h3 {
    overflow-wrap: anywhere;
    word-break: break-word;
}
@media(max-width:760px){
    #main{
        width:100%;
        margin:10px;
        
    }
    
}
input{
    padding: 4px;
}
button{
    margin: 3px;
}

</style>