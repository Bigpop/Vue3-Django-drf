<template>
<br>
  <div v-for="whisper in info" v-bind:key="whisper.id" id="whispers">
    
    <div class="grid">
      <div class="content">{{ whisper.content }}</div>
      <div class="time">
        {{ formatted_time(whisper.c_time) }}
      </div>
    </div>
    <div class="hr-container">
      <hr />
    </div>
  </div>

  <!-- <div id="paginator">
        <span v-if="is_page_exists('previous')">
            <router-link :to="get_path('previous')">
                Prev
            </router-link>
        </span>
        <span class="current-page">
            {{ get_page_param('current') }}
        </span>
        <span v-if="is_page_exists('next')">
            <router-link :to="get_path('next')">
                Next
            </router-link>
        </span>
    </div> -->
</template>

<script>
import axios from "axios";

export default {
  name: "WhisperList",
  data: function () {
    return {
      info: "",
    };
  },
  mounted() {
    this.get_whisper_data();
  },
  methods: {
    formatted_time: function (iso_date_string) {
      const date = new Date(iso_date_string);
      var datetext = date.toTimeString();
      datetext = datetext.split(" ")[0];
      var h = datetext.split(":")[0];
      var m = datetext.split(":")[1];
      datetext = h + " : " + m;

      return date.toLocaleDateString() + "\n" + datetext;
    },
    is_page_exists(direction) {
      if (direction === "next") {
        return this.info.next !== null;
      }
      return this.info.previous !== null;
    },
    get_page_param: function (direction) {
      try {
        let url_string;
        switch (direction) {
          case "next":
            url_string = this.info.next;
            break;
          case "previous":
            url_string = this.info.previous;
            break;
          default:
            return this.$route.query.page;
        }
        const url = new URL(url_string);
        return url.searchParams.get("page");
      } catch (err) {
        return;
      }
    },
    get_path: function (direction) {
      let url = "";
      try {
        switch (direction) {
          case "next":
            if (this.info.next !== undefined) {
              url += new URL(this.info.next).search;
            }
            break;
          case "previous":
            if (this.info.previous !== undefined) {
              url += new URL(this.info.previous).search;
            }
            break;
        }
      } catch {
        return url;
      }
      return url;
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
hr {
  display: block;
  height: 1px;
  border: 0;
  border-top: 1px solid rgba(143, 102, 102, 0.5);
  margin: 1em 0;
  padding: 0;
}
#paginator {
  text-align: center;
  padding-top: 50px;
}
a {
  color: black;
}
.current-page {
  font-size: x-large;
  font-weight: bold;
  padding-left: 10px;
  padding-right: 10px;
}
.grid {
  display: grid;
  grid-template-columns: 3fr 1fr;
  padding-left: 15%;
  padding-right: 15%;
  width: 70%;
  display: flex;

}
.content {
  width: 85%;
  word-wrap: break-word;
  word-break: normal;
}
.time {
  white-space: pre-line;
  padding-left: 5%;
  font-size: xx-small;
  color: #c8c8c8;
  float: right;
}
.hr-container {
  padding-left: 15%;
  padding-right: 15%;
}
</style>