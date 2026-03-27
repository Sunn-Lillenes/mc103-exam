const hre = require("hardhat");

async function main() {
  const tokenAddress = "0x38473A9A19Cf8fDC41f793dFADB61934E87A1a41";
  const recipient = "0x4c2bC7215DC111b42482e4130174832A5680dcc9";

  const token = await hre.ethers.getContractAt("SJLToken", tokenAddress);

  const amount = hre.ethers.parseUnits("1000", 18);
  const tx = await token.transfer(recipient, amount);
  console.log("Transaction sent:", tx.hash);
  await tx.wait();
  console.log("Transfer confirmed! Sent 1000 SJL to", recipient);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
