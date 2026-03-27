
const hre = require("hardhat");

async function main() {

  const Token = await hre.ethers.getContractFactory("SJLToken");

  const token = await Token.deploy();

  await token.waitForDeployment();

  const address = await token.getAddress();

  console.log("SJLToken deployed to:", address);

}

main().catch((error) => {

  console.error(error);

  process.exitCode = 1;

});

