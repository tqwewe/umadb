[![UmaDB Logo](images/UmaDB-brand-figure-torso-and-lettering.png)](https://umadb.io)

# What is UmaDB?

**UmaDB** is a specialist open-source event store built for **dynamic consistency boundaries**.

UmaDB supports event-driven architectures where consistency rules can adapt dynamically to
business needs, rather than being hardwired into the database.

UmaDB directly implements the [independent specification](https://dcb.events/specification/) for
[Dynamic Consistency Boundaries](https://dcb.events) created by Bastian Waidelich, Sara Pellegrini,
and Paul Grimshaw.

UmaDB stores events in an append-only sequence, indexed by monotonically increasing gapless positions,
and can be tagged for fast, precise filtering.

UmaDB offers:

* **High-performance concurrency** with non-blocking reads and writes
* **Optimistic concurrency control** to prevent simultaneous write conflicts
* **Dynamic business-rule enforcement** via query-driven append conditions
* **Real-time subscriptions** with seamless catch-up and continuous delivery
* **OSI-approved permissive open-source licenses** (MIT and Apache License 2.0) 

UmaDB makes new events fully durable before acknowledgements are returned to clients.

## Website

Please visit the [UmaDB website](https://umadb.io) for more information.

## License

Licensed under either of

- Apache License, Version 2.0 (LICENSE-APACHE or http://www.apache.org/licenses/LICENSE-2.0)
- MIT license (LICENSE-MIT or http://opensource.org/licenses/MIT)

at your option.

### Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in UmaDB by you, as defined in the Apache-2.0 license, shall be dual licensed as above, without any additional terms or conditions.
