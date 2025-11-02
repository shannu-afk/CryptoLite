const txForm = document.getElementById("txForm");
const mineBtn = document.getElementById("mineBtn");

txForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const formData = new FormData(txForm);
  const data = Object.fromEntries(formData.entries());
  
  const res = await fetch("/add_transaction", {
    method: "POST",
    body: new URLSearchParams(data)
  });
  const json = await res.json();
  Swal.fire("Success!", json.message, "success").then(() => {
    location.reload();
  });
});

mineBtn.addEventListener("click", async () => {
  Swal.fire({title: "Mining block...", text: "Please wait", allowOutsideClick: false, didOpen: () => Swal.showLoading()});
  const res = await fetch("/mine_block", {method: "POST"});
  const json = await res.json();
  Swal.fire("Done!", json.message, "success").then(() => {
    location.reload();
  });
});
