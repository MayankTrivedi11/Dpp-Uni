const hre = require("hardhat");

async function main() {
  const CourseManagement = await hre.ethers.getContractFactory("CourseManagement");
  const courseManagement = await CourseManagement.deploy();

  await courseManagement.deployed();
  console.log("CourseManagement deployed to:", courseManagement.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
