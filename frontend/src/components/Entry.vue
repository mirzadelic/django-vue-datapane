<template>
  <div>
    <v-form @submit.prevent="addOrUpdate($v)">
      <v-row>
        <v-col cols="12" md="4">
          <v-text-field
            v-model="entryData.name"
            label="Name"
            :error="$v.entryData.name.$error"></v-text-field>
        </v-col>
        <v-col cols="12" md="4">
          <v-text-field
            v-model="entryData.email"
            type="email"
            label="Email address"
            :error="$v.entryData.email.$error"></v-text-field>
        </v-col>
        <v-col cols="12" md="4">
          <v-text-field
            v-model="entryData.age"
            type="number"
            label="Age"
            :error="$v.entryData.name.$error"></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="4">
          <v-btn color="primary" type="submit" dark>
            {{ entryData.id ? 'Edit' : 'Add' }}
          </v-btn>
          <v-btn
            v-if="entryData.id"
            @click="clearEntry()"
            color="warning"
            class="float-right"
            dark>Clear update</v-btn>
        </v-col>
      </v-row>
    </v-form>
    <v-row>
        <v-col>
            <v-simple-table v-if="!loading">
              <template v-slot:default>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Age</th>
                    <th width="20%">Actions</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="item in entries" :key="item.id">
                    <td>{{ item.name }}</td>
                    <td>{{ item.email }}</td>
                    <td>{{ item.age }}</td>
                    <td>
                      <v-btn
                        color="primary"
                        @click="editEntryMode(item)"
                        dark
                        small>Edit</v-btn>
                      <v-btn
                        color="red"
                        class="ml-2"
                        @click="deleteEntry(item)"
                        dark
                        small>Delete</v-btn>
                    </td>
                  </tr>
                </tbody>
              </template>
            </v-simple-table>
            <p v-if="loading">Loading data...</p>
        </v-col>
    </v-row>
  </div>
</template>

<script>
  import axios from '@/axios'
  import { required, email, integer } from 'vuelidate/lib/validators'
  const entryApiUrl = 'api/v1/app/entry/'

  export default {
    name: 'Entry',
    props: {
    },
    data: () => ({
      loading: true,
      entryData: {},
      entries: []
    }),
    validations: {
      entryData: {
        name: {
          required
        },
        email: {
          required,
          email
        },
        age: {
          required,
          integer
        },
      }
    },
    created () {
      this.clearEntry()
      this.getData()
    },
    methods: {
      clearEntry () {
        this.entryData = {
          name: '',
          email: '',
          age: null
        }
      },
      getData () {
        this.loading = true
        axios.get(entryApiUrl).then(response => {
          this.entries = response.data
        })
        this.loading = false
      },
      editEntryMode (entry) {
        this.entryData = Object.assign({}, entry)
      },
      addOrUpdate($v) {
        $v.entryData.$touch()
        if ($v.entryData.$invalid) return

        var method = 'post'
        var url = entryApiUrl
        if (this.entryData.id) {
          method = 'put'
          url += `${this.entryData.id}/`
        }

        return axios({
          method: method,
          url: url,
          data: this.entryData
        }).then(() => {
          this.clearEntry()
          this.getData()
          $v.entryData.$reset()
        }).catch(() => {
            alert('Error, please try again.');
        })
      },
      deleteEntry (entry) {
        axios.delete(`${entryApiUrl}${entry.id}/`).then(() => {
          this.clearEntry()
          this.getData()
        }).catch(() => {
            alert('Error, please try again.');
        })
      }
    }
  }
</script>
