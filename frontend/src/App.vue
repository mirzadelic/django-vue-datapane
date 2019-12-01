<template>
  <v-app id="inspire">
    <v-navigation-drawer
      app
      left
    >
      <v-list dense>
        <v-list-item :to="{name: 'Home'}">

          <v-list-item-content>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item :to="{name: 'CSVParser'}">
          <v-list-item-content>
            <v-list-item-title>CSV Uploader</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item :to="{name: 'Entry'}">
          <v-list-item-content>
            <v-list-item-title>Entry Form</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      color="cyan"
      dark
    >

      <v-spacer />

      <v-toolbar-title>Application</v-toolbar-title>
    </v-app-bar>

    <v-content>
      <v-container>
        <v-row>
          <v-col>
            <router-view />
          </v-col>
        </v-row>
      </v-container>
    </v-content>

    <v-footer
      color="cyan"
      app
    >
      <v-spacer />

      <span class="white--text">&copy; 2019</span>
    </v-footer>
  </v-app>
</template>

<script>
  export default {
    name: 'App',
    props: {
    },
    data: () => ({

    }),
  }
</script>
