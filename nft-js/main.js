const Moralis = require("moralis").default;
const { EvmChain } = require("@moralisweb3/common-evm-utils");

const runApp = async () => {
  await Moralis.start({
    apiKey: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub25jZSI6IjI0Mzc4NzgyLTNjZmItNDIwZS04ZjgyLWJkYTk0MjNhNmM0NyIsIm9yZ0lkIjoiMjI2MDQ0IiwidXNlcklkIjoiMjI2NDEwIiwidHlwZUlkIjoiOGFhMTA4ODctZjBiNi00YzNmLThlN2YtYTkxZjgyY2Q0OGQ2IiwidHlwZSI6IlBST0pFQ1QiLCJpYXQiOjE2OTc4NzY3NTQsImV4cCI6NDg1MzYzNjc1NH0.8DHNFny4xHmVK3eGDPXbzbRKdzG3VPE5-hqvQCCAJ3w",
    // ...and any other configuration
  });

  const allNFTs = [];

  const address = "0xE21B74060Cdec9D96F865963d8e5F7Def37F0895";

  const chains = [EvmChain.ETHEREUM, EvmChain.BSC, EvmChain.POLYGON];

  for (const chain of chains) {
    const response = await Moralis.EvmApi.nft.getWalletNFTs({
      address,
      chain,
    });

    allNFTs.push(response);
  }

  console.log(allNFTs);
};

runApp();
