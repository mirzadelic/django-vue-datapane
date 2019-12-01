<template>
  <div>
    <v-form @submit.prevent="addOrUpdate($v)">
      <v-row>
        <v-col cols="12">
          <v-file-input
            label="File input"
            v-model="file"
            accept=".csv"
            @change="dataLoaded = false"></v-file-input>
        </v-col>
        <v-col cols="12">
          <v-btn color="primary" v-on:click="uploadFile()" dark>
            Upload and process
          </v-btn>
        </v-col>
      </v-row>
    </v-form>
    <v-row v-if="dataLoaded">
        <v-col>
          <v-simple-table>
            <template v-slot:default>
              <thead>
                <tr>
                  <th v-for="header in headers" :key="header">{{ header }}</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in data" :key="item.id">
                  <td v-for="header in headers" :key="header">{{ item[header] }}</td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
        </v-col>
    </v-row>
  </div>
</template>

<script>
  import axios from '@/axios'
  const csvUploadApiUrl = 'api/v1/app/csv-parser/'

  export default {
    name: 'CSVParser',
    props: {
    },
    data: () => ({
      file: null,
      dataLoaded: false,
      headers: [],
      data: []
    }),
    methods: {
      uploadFile() {
        let formData = new FormData()
        formData.set('file', this.file)

        axios.post(csvUploadApiUrl, formData, {
          headers: {'Content-Type': 'multipart/form-data'}
        }).then((response) => {
          this.headers = response.data['headers'];
          this.data = response.data['data'];
          this.dataLoaded = true;
        }).catch(() => {
          alert('Error, please try again.');
        })
      }
    }
  }
</script>
