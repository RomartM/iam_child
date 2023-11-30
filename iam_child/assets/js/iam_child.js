
fetch("/api/method/iam_child.api.general.common").then((response) => response.json())
  .then((data) => {
    cur_frm.fields_dict["associated_systems"].grid.get_field("smart_system").get_query = function(doc) {
    return {
            filters: {
                "system_name": data?.message?.system_name
            }
        }
    }
});