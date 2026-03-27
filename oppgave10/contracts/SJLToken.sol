
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract SJLToken is ERC20 {
    constructor() ERC20("SJL Token", "SJL") {
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }
}
