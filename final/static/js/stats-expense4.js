const renderChart4 = (data, labels) => {
  var ctx = document.getElementById("myChart4").getContext("2d");
  var myChart4 = new Chart(ctx, {
    type: "pie",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Today's Expenses",
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
        text: "Today's Expenses",
      },
    },
  });
};

const getChartData4 = () => {
  console.log("fetching");
  fetch("/expense_category_summary_day") // Use the endpoint that provides data for the last month
    .then((res) => res.json())
    .then((results) => {
      console.log("results", results);
      const category_data = results.expense_category_data;
      const [labels, data] = [
        Object.keys(category_data),
        Object.values(category_data),
      ];

      renderChart4(data, labels);
    });
};

document.onload = getChartData4();
