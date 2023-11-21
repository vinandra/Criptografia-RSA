process.stdin.setEncoding("utf8");

let a: number | undefined;
let b: number | undefined;

console.log("Masukkan nilai a: ");

let inputs: "inputA" | "inputB" = "inputA";

process.stdin.on("data", (data: string) => {
  const trimmedData = data.trim();
  const parsedData = parseFloat(trimmedData);

  if (isNaN(parsedData)) {
    console.log("Mohon masukkan nilai numerik.");
    process.exit();
  }

  if (inputs === "inputA") {
    a = parsedData;
    inputs = "inputB";
    console.log("Masukkan nilai b: ");
  } else {
    b = parsedData;
    console.log(`Hasil pertambahan a + b: ${a! + b!}`);
    process.exit();
  }
});

process.stdin.resume();
