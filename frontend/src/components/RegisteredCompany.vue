<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import api from '@/services/api'
import LoadingSpinner from '@/components/LoadingSpinner.vue'
import DataCardList from '@/components/DataCardList.vue'
const rcusers = ref([])
const route = useRoute()
const message = ref('')
const isLoading = ref(false)

const fields = [
    { label: 'Company ID', key: 'user_id' },
    { label: 'Company Name', key: 'user_name' },
    { label: 'Company Email', key: 'user_email' },
]



// fetching company
// get request

const fetchUsers = async () => {
    try {
        isLoading.value = true
        message.value = ' '
        const response = await api.get(
            '/admin/registered_company',
            {
                params: {
                    search: (route.query.search || '').toString()
                },
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`
                }
            }
        )

        rcusers.value = response.data
    } catch (err) {
        console.log(err)
    } finally {
        isLoading.value = false
    }
}

function blackList(){
    return
}


// delete request 
// deleting company____________________

async function removeCompany(user_id) {
    const token = localStorage.getItem('token')
    if(!token){
        localStorage.clear()
        window.location.href = '/login'
        return
    }

    try{
        message.value = ' '
        const response = await api.delete(
            `/admin/remove_company/${user_id}`,
            {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            }
        )
        message.value = response.data?.message || 'company removed successfully'
        fetchUsers()
    } catch (err) {
        message.value = err.response?.data?.message || 'failed to remove company'
    }
}

onMounted(() => {
    fetchUsers()
})

watch(
    () => route.query.search,
    () => {
        fetchUsers()
    }
)
</script>

<template>
    <div id="registered_company">
        <p v-if="message">{{ message }}</p>
        <p style="color: chocolate;">Total Number Of Registered Company/Recruiter is {{ rcusers.length }}</p>

        <h1>Registered Companys</h1><br>
        <div v-if="isLoading" class="inline-loader">
            <LoadingSpinner label="Loading" />
        </div>
        <DataCardList :items="rcusers" :fields="fields" item-key="user_id" empty-text="no records">
            <template #actions="{ item }">
                <button class="dngr" @click="blackList(item.user_id)">blacklist</button>
                <button class="dngr" @click="removeCompany(item.user_id)">remove</button>
            </template>
        </DataCardList>
    </div>
</template>
<style>


#registered_company {
    margin-top: 30px;
}

#dngr {
    color: red;
}

.inline-loader{
    margin: 8px 0 12px;
}
</style>