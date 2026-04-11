<script setup>
import { ref,onMounted } from 'vue'
import axios from 'axios'

const company = ref({
    company_id: '',
    hr_no: '',
    company_description: '',
    website: '',
})
const message = ref('')

async function fetchCompany() {
    const token = localStorage.getItem('token')
    const id=localStorage.getItem('user_id')
    if (!token) {
        localStorage.clear()
        window.location.href = '/login'
        return
    }

    try {
        const response = await axios.get(`http://localhost:5000/company_profile/${id}`, {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        })

        
        if (response.data?.company_id !== undefined) {
            company.value = response.data
            message.value = ''
        } else {
            message.value = response.data?.message || ''
        }
    } catch (err) {
        if (err.response?.status === 401) {
            message.value = 'Token expired, please relogin'
            localStorage.clear()
            window.location.href = '/login'
            return
        }
        message.value = err.response?.data?.message || 'Failed to fetch profile'
        console.error(err)
    }
}


async function updateCompany() {
    const token = localStorage.getItem('token')
    if (!token) {
        localStorage.clear()
        window.location.href = '/login'
        return
    }

    try {
        const response = await axios.put('http://localhost:5000/company/profile', company.value, {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        })

        message.value = response.data?.message || 'Updated successfully'
        await fetchCompany()
    } catch (err) {
        if (err.response?.status === 401) {
            message.value = 'Token expired, please relogin'
            localStorage.clear()
            window.location.href = '/login'
            return
        }
        message.value = err.response?.data?.message || 'Update failed'
        console.error(err)
    }
}

onMounted(() => {
    fetchCompany()
})

</script>

<template>
    <div id="parent_div">
        <h1>Company Profile</h1>
        <p v-if="message" class="msg">{{ message }}</p>

        <form @submit.prevent="updateCompany">
            <p>Company Id: {{ company.company_id }}</p>


            <label for="phone">HR No</label><br />
            <input type="tel" id="phone" placeholder="your phone number" v-model="company.hr_no" /><br />

            <label for="company_description">company_description</label><br />
            <textarea name="company_description" id="company_description" cols="55" rows="3" placeholder="Enter your full company_description here"
                v-model="company.company_description"></textarea><br />

            <label for="website">Social Profile</label><br />
            <input type="text" id="website" placeholder="https://linkedin.in/example"
                v-model="company.website" /><br /><br />

            <button type="submit">update</button>
        </form>
    </div>
</template>

<style scoped>
input {
    margin: 1px;
    color: gray;
    width: 250px;
    line-height: 30px;
}

label {
    color: #2980b9;
}

button {
    font-weight: bold;
    border: 2px solid cadetblue;
    text-decoration: underline;
}

textarea {
    margin: 1px;
    border: 1px solid #2980b9;
    padding: 3px;
    color: gray;
}

.msg {
    color: chocolate;
}
.spl{
    text-decoration: underline;
    color: #2980b9;
}
.spl:hover{
    color: cadetblue;
    /* transform: scale(1.1); */
    /* text-decoration: overline; */
}

@media(max-width:770px){
    input{
        width: 280px;
    }
    #parent_div{
        padding: 20px;
    }
    textarea{
        width: 280px;
    }
}

</style>
