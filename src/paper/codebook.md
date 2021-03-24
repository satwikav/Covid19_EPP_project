## Codebook for Covid-19 Policy Stringency Index for Germany
This codebook is constructed on the basis of the Fedral policies for contact restrictions that we have collected to calculate the Stringecy Index. The dataset that we have collected consists of 9 indicators that have been divided into 3 main groups:
- [E: Containment policies for schools](#containment-policies-for-schools)
- S: Containment policies for entertainment and shopping (public activities)
- R: Containment policies for private gatherings
<p align="justify">
All the 9 indicators are recorded on an ordinal scale according to the level of policy stringency. A value of 0 always indicates no contact restriction; values of 1 or larger represent an increase in the policy’s level of contact stringency. The data set further assigns each policy entry three additional values, namely two binary variables, the flag and the recorded flag, as well as the maximum value of the policy’s affiliated indicator. While the flag variable distinguishes between indicators that are not characterized by their geographic scope (0) and those that are (1), the recorded flag indicates whether an indicator was implemented at the state (0) or national (1) level.
</p>

---
### Containment policies for schools

| ID | Name | Description | Measurement | Coding |
| --- | --- | --- | --- | --- |
| E1 | `SI_E1` | Record closings of kitas | Ordinal scale | 0 - no measures <br/>1 - recommend closing <br/>2 - require closing (only some levels or categories, eg just high school, or just public schools) <br/>3 - require closing all levels <br/>Blank - no data |
| | `flag_E1` | | Binary flag for geographic scope | 0 - targeted <br/>1 - general <br/>-100 - no data |
| | `recorded_flag_E1` | | Binary flag for policy implementation | 0 - state level <br/>1 - national level <br/>-100 - no data|
| E2 | `SI_E2` | Record closings of elementary schools | Ordinal scale | 0 - no measures <br/>1 - recommend closing (or recommend work from home) <br/>2 - require closing (or work from home) for some sectors or categories of workers <br/>3 - require closing (or work from home) for all-but-essential workplaces (eg grocery stores, doctors) <br/>Blank - no data |
| | `flag_E2` | | Binary flag for geographic scope | 0 - targeted <br/>1 - general <br/>-100 - no data |
| | `recorded_flag_E2` | | Binary flag for policy implementation|0 - state level <br/>1 - national level <br/>-100 - no data |
| E3 | `SI_E3` | Record closings of schools for grades 5 to 10 | Ordinal scale | 0 - no measures <br/>1 - recommend cancelling <br/>2 - require cancelling <br/>Blank - no data |
| | `flag_E3` | | Binary flag for geographic scope |0 - targeted <br/>1 - general <br/>-100 - no data |
| | `recorded_flag_E3` | | Binary flag for policy implementation | 0 - state level <br/>1 - national level <br/>-100 - no data|
| E4 | `SI_E4` | Record closings of schools for grades 11 to 12/13| Ordinal scale | 0 - no restrictions <br/>1 - restrictions on very large gatherings (the limit is above 1000 people) <br/>2 - restrictions on gatherings between 101-1000 people <br/>3 - restrictions on gatherings between 11-100 people <br/>4 - restrictions on gatherings of 10 people or less <br/>Blank - no data |
| | `flag_E4` | | Binary flag for geographic scope | 0 - targeted <br/>1 - general <br/>-100 - no data |
| | `recorded_flag_E4` | | Binary flag for policy implementation | 0 - state level <br/>1 - national level <br/>-100 - no data |

---
