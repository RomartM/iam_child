function waitForFieldsDict() {
    return new Promise((resolve) => {
        const checkFieldsDict = setInterval(() => {
            if (cur_frm && cur_frm?.fields_dict) {
                clearInterval(checkFieldsDict);
                resolve();
            }
        }, 100); // Check every 100 milliseconds
    });
}

function fetchAndModify() {
    fetch("/api/method/iam_child.api.general.common")
        .then((response) => response.json())
        .then((data) => {
            cur_frm.fields_dict["associated_systems"].grid.get_field("smart_system").get_query = function(doc) {
                return {
                    filters: {
                        "system_name": data?.message?.system_name
                    }
                };
            };
        })
        .catch((error) => {
            console.error("Error fetching data:", error);
        });
}

waitForFieldsDict().then(fetchAndModify);
