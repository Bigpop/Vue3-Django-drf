<template>
  <div class="grid">
    <div class="toc">
      <div v-for="origin in origins" v-bind:key="origin.id" class="sub-grid">
        <div v-on:click="get_trans_tree(origin.id)" class="title">
          {{ origin.title }}
        </div>
        <button class="likes">{{ origin.likes }} likes</button>
      </div>
    </div>

    <div class="grid-right">
      <div class="grid-origin">
        <pre style="text-align: left; padding: 2%;margin: 0; font-size: x-large">{{
          trans_tree.content
        }}</pre>
        <p style="text-align: right; padding-right: 2%">
          {{ trans_tree.title }}
        </p>
      </div>
      <br /><br /><br />
      <div
        v-for="trans in trans_tree.child_list"
        v-bind:key="trans.id"
        class="grid-trans"
      >
        <div class="trans">
          <pre style="text-align: left; padding: 2%; margin: 0;font-size: x-large">{{
            trans.content
          }}</pre>
          <p style="text-align: right; padding-right: 2%; margin: 0">
            {{ trans.content_source }}
          </p>
          <p style="text-align: right; padding-right: 2%; margin: 0">
            {{trans.uploader_id}} uploaded at {{ formatted_time(trans.c_time) }}
          </p>
          <p style="text-align: right; padding-right: 2%; margin: 0">
            {{ trans.likes }} likes
          </p>
          
        </div>
        <br>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "Origins",
  data: function () {
    return {
      origins: null,
      trans_tree: "",
    };
  },

  async mounted() {
    axios
      .get("/api/transforum/origin-list")
      .then((response) => {
        this.origins = response.data;
        this.get_trans_tree(this.origins[0]["id"]);
      })
      .catch(function (error) {
        console.log(error);
      });
  },
  methods: {
    greet: function (event) {
      // `this` inside methods points to the Vue instance
      alert("Hello " + this.name + "!");
      // `event` is the native DOM event
      if (event) {
        alert(event.target.tagName);
      }
    },
    get_trans_tree: function (id) {
      axios
        .get("/api/transforum/" + id.toString())
        .then((response) => {
          this.trans_tree = response.data;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    formatted_time: function (iso_date_string) {
      const date = new Date(iso_date_string);
      var datetext = date.toTimeString();
      datetext = datetext.split(" ")[0];
      var h = datetext.split(":")[0];
      var m = datetext.split(":")[1];
      datetext = h + " : " + m;

      return date.toLocaleDateString() + "\n" + datetext;
    },
    get_whisper_data: function () {
      let url = "/api/whisper/all";

      let params = new URLSearchParams();
      params.appendIfExists("page", this.$route.query.page);
      params.appendIfExists("search", this.$route.query.search);

      const paramsString = params.toString();
      if (paramsString.charAt(0) !== "") {
        url += "/?" + paramsString;
      }

      axios
        .get(url)
        .then((response) => (this.info = response.data))
        .then(console.log("test"));
    },
  },
  watch: {},
};
</script>

<style scoped>
.grid {
  display: grid;
  grid-template-columns: 1fr 3fr;
}
.sub-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

.title:hover {
  color: green;

  cursor: pointer;
}
.likes:hover {
  background: rgb(255, 0, 0);
  cursor: pointer;
}

.grid-right {
  padding: 3%;
}
.grid-origin {
  box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px, rgb(51, 51, 51) 0px 0px 0px 3px;
  border-radius: 10px;
}
.trans {
  box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;

  border-radius: 10px;
}
</style>