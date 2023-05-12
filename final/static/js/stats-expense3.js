const renderChart3 = (data, labels) => {
  var ctx = document.getElementById("myChart3").getContext("2d");
  var myChart3 = new Chart(ctx, {
    type: "line",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Expenses for Last Month",
          data: data,
          backgroundColor: [
            "rgba(255, 99, 132, 0.4)",
            "rgba(54, 162, 235, 0.4)",
            "rgba(255, 206, 86, 0.4)",
            "rgba(75, 192, 192, 0.4)",
            "rgba(153, 102, 255, 0.4)",
            "rgba(255, 159, 64, 0.4)",
          ],
          borderColor: [
            "rgba(255, 99, 132, 1)",
            "rgba(54, 162, 235, 1)",
            "rgba(255, 206, 86, 1)",
            "rgba(75, 192, 192, 1)",
            "rgba(153, 102, 255, 1)",
            "rgba(255, 159, 64, 1)",
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      title: {
        display: true,
        text: "Expenses for Last Month",
      },
    },
  });
};

const getChartData3 = () => {
  console.log("fetching");
  fetch("/expense_category_summary_month") // Use the endpoint that provides data for the last month
    .then((res) => res.json())
    .then((results) => {
      console.log("results", results);
      const category_data = results.expense_category_data;
      const [labels, data] = [
        Object.keys(category_data),
        Object.values(category_data),
      ];

      renderChart3(data, labels);
    });
};

document.onload = getChartData3();
