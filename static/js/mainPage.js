function totaldeisel() {
  var x = parseFloat(document.getElementById("HSDpump").value);
  var y = parseFloat(document.getElementById("DeiselDRate").value);
  var z = parseFloat(document.getElementById("CashOnHand").value) 
  document.getElementById("TotalDeisel").value = (x * y)+z;
}

function totalExpense() {
  var a = parseFloat(document.getElementById("TotalDeisel").value);
  var b = parseFloat(document.getElementById("DriverPayment").value);
  var c = parseFloat(document.getElementById("Tax").value);
  var d = parseFloat(document.getElementById("OtherExpenses").value);
  
  document.getElementById("TotalBillAmnt").value = a+b+c+d  ;
}

function IgstAmount() {
  var a = parseFloat(document.getElementById("Taxableamnt").value);
  
  document.getElementById("Igst").value = (a*0.18)  ;
  
}

function billingAmount() {
  var a = parseFloat(document.getElementById("Taxableamnt").value);
  
  
  document.getElementById("TotalBillingAmount").value = (a*0.18)+a  ;
}